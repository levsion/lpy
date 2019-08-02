from fabric import *
from invoke import *
import re

project_config = {
    'kuaiyong':{
        'hosts':['root@172.111.164.10:22'],
        'passwords':['123456'],
        'private_keys':["/Users/levsion/.ssh/id_rsa.pub"]
    },
    'gameweb':{
        'hosts':['root@172.111.164.10:22','root@172.111.164.11:22','root@172.111.164.12:22'],
        'passwords':['123456','123456','123456'],
        'private_keys':["/home/myuser/.ssh/private.key","/home/myuser/.ssh/private.key","/home/myuser/.ssh/private.key"]
    }
}

project_local_dir = {
    'kuaiyong':'/Users/levsion/Documents/code/git_php/git_levsion1/kuaiyong',
    'gameweb':'/data/wwwroot/gameweb'
}
project_remote_dir = {
    'kuaiyong':'/mydata/app/kuaiyong',
    'gameweb':'/data/wwwroot/gameweb'
}

@task()
def hello(c,project):

    print "hello fabric",project


def web_conn(project):
    conn_list = []
    for k in range(len(project_config[project]['hosts'])):
        #conn = Connection(project_config[project]['hosts'][k], connect_kwargs={"password": project_config[project]['passwords'][k]})
        conn = Connection(project_config[project]['hosts'][k], connect_kwargs={"key_filename": project_config[project]['private_keys'][k]})
        conn_list.append(conn)
    return conn_list

def projects(project):
    def wraped(func):
        def inner(*args, **kwargs):
            if project=='kuaiyong':
                run("cd " + project_local_dir[project])
            else:
                run("cd " + project_local_dir[project])
            conn_list = web_conn(project)
            func(conn_list)
        return inner
    return wraped



def get_tag_list(c,project):
    with c.cd(project_local_dir[project]):
        c.run("git pull", hide=True, warn=True)
        tag_str = c.run("git tag", hide=True, warn=True)
        if tag_str:
            tag_str = tag_str.stdout.strip()
            tag_list = tag_str.split("\n")
            return tag_list

def get_tag_info(c,tag,project):
    with c.cd(project_local_dir[project]):
        gg = c.run("git show "+tag,hide=True,warn=True)
        return gg.stdout.strip()


@task
def go_tag_list(c,project):
    if not project_config.has_key(project):
        print("Error: project "+project+" not exist")
        quit()
    with c.cd(project_local_dir[project]):
        c.run("git pull", hide=True, warn=True)
        tag_str = c.run("git tag", hide=True, warn=True)
        if tag_str:
            tag_str = tag_str.stdout.strip()
            print tag_str

@task
def create_tag(c,project,tag):
    if not project_config.has_key(project):
        print("Error: project "+project+" not exist")
        quit()
    if not re.match(r'v[\d]{1,2}\.[\d]{1,2}\.[\d]{1,2}$',tag):
        print("Error: tag format error !!!")
        quit()
    with c.cd(project_local_dir[project]):
        tag_list = get_tag_list(c,project)
        if tag in tag_list:
            print("Error: tag "+tag+" already exists !!!")
            quit()
        if tag <= tag_list[-1]:
            print("Error: tag must bigger than " + tag_list[-1])
            quit()
        c.run("git checkout master")
        c.run("git pull")
        c.run("git tag -a "+tag+" -m \"release version "+tag+"\"")
        c.run("git push origin --tags")
        print("Create tag "+tag+" success !!!")

@task
def del_tag(c,project,tag):
    if not project_config.has_key(project):
        print("Error: project "+project+" not exist")
        quit()
    if not re.match(r'v[\d]{1,2}\.[\d]{1,2}\.[\d]{1,2}',tag):
        print("Error: tag format error !!!")
        quit()
    with c.cd(project_local_dir[project]):
        c.run("git tag -d "+tag)
        c.run("git push origin :" + tag)

@task
def deploy(c,project):
    if not project_config.has_key(project):
        print("Error: project " + project + " not exist")
        quit()
    tag_list = get_tag_list(c,project)
    tag =  tag_list[-1]
    conn_list = web_conn(project)
    for conn in conn_list:
        with conn.cd(project_remote_dir[project]):
            host = conn.host
            print("The host "+host+" deploy begin tag: "+tag)
            conn.run("git fetch origin tag "+tag)
            conn.run("git checkout "+ tag)
            print("The host "+host+" deploy success !!!")
    print("All hosts deploy success !!!")

@task
def rollback(c,project):
    if not project_config.has_key(project):
        print("Error: project "+project+" not exist")
        quit()
    tag_list = get_tag_list(c,project)
    tag = tag_list[-2]
    del_tag = tag_list[-1]
    conn_list = web_conn(project)
    for conn in conn_list:
        with conn.cd(project_remote_dir[project]):
            print("Begin rollback, checkout " + tag)
            conn.run("git pull",hide=True,warn=True)
            conn.run("git checkout " + tag)
            print("checkout end")
    with c.cd(project_local_dir[project]):
        c.run("git tag -d "+del_tag)
        c.run("git push origin :" + del_tag)
        tag_info = get_tag_info(c,tag,project)
        if tag_info:
            rs = re.findall(r"commit\s+([0-9a-zA-Z]+)[\n|\s]*", tag_info, re.S|re.I)
            if len(rs)>0:
                commit_id = rs[0]
                c.run("git checkout master",hide=True,warn=True)
                c.run("git reset --hard " + commit_id)
                c.run("git push -f")
                print("Rollback end "+tag+": "+commit_id)