from fabric import *
from invoke import *
import re

private_key_path = "/Users/levsion/.ssh/id_rsa.pub"
git_path = "/Users/levsion/Documents/code/wangtuo"

project_config = {
    'kuaiyong':{
        'hosts':['root@172.111.164.10:22'],
        'passwords':['123456'],
        'private_keys':[private_key_path]
    },
    'jmweb':{
        'hosts':['root@47.111.166.180:22022','root@47.111.168.155:22022','root@47.111.168.25:22022','root@47.111.166.185:22022'],
        'passwords':['123456','123456','123456','123456'],
        'private_keys':[private_key_path,private_key_path,private_key_path,private_key_path]
    },
    'jmh5':{
        'hosts':['root@47.111.166.180:22022','root@47.111.168.155:22022','root@47.111.168.25:22022'],
        'passwords':['123456','123456','123456'],
        'private_keys':[private_key_path,private_key_path,private_key_path]
    },
    'jmadmin':{
        'hosts':['root@47.111.166.185:22022'],
        'passwords':['123456'],
        'private_keys':[private_key_path]
    },
    'jmpromote':{
        'hosts':['root@47.111.166.185:22022'],
        'passwords':['123456'],
        'private_keys':[private_key_path]
    },
    'gpublish':{
        'hosts':['root@47.111.166.185:22022'],
        'passwords':['123456'],
        'private_keys':[private_key_path]
    },
    'publishadmin':{
        'hosts':['root@47.111.166.185:22022'],
        'passwords':['123456'],
        'private_keys':[private_key_path]
    },
    'gm_h5_web':{
        'hosts':['root@47.111.166.185:22022'],
        'passwords':['123456'],
        'private_keys':[private_key_path]
    },
    'gmapi':{
        'hosts':['root@47.111.166.185:22022'],
        'passwords':['123456'],
        'private_keys':[private_key_path]
    },
    'gmadmin':{
        'hosts':['root@47.111.166.185:22022'],
        'passwords':['123456'],
        'private_keys':[private_key_path]
    }
}

project_local_dir = {
    'kuaiyong':'/Users/levsion/Documents/code/git_php/git_levsion1/kuaiyong',
    'jmweb':git_path + '/jmweb',
    'jmh5':git_path + '/jmh5',
    'jmadmin':git_path + '/jmadmin',
    'jmpromote':git_path + '/jmpromote',
    'gpublish':git_path + '/gpublish',
    'publishadmin':git_path + '/publishadmin',
    'gm_h5_web':git_path + '/gm_h5_web',
    'gmapi':git_path + '/gmapi',
    'gmadmin':git_path + '/gmadmin',
}
project_remote_dir = {
    'kuaiyong':'/mydata/app/kuaiyong',
    'jmweb':'/data/wwwroot/jmweb',
    'jmh5':'/data/wwwroot/jmh5',
    'jmadmin':'/data/wwwroot/jmadmin',
    'jmpromote':'/data/wwwroot/jmpromote',
    'gpublish':'/data/wwwroot/gpublish',
    'publishadmin':'/data/wwwroot/publishadmin',
    'gm_h5_web':'/data/wwwroot/gm_h5_web',
    'gmapi':'/data/wwwroot/gmapi',
    'gmadmin':'/data/wwwroot/gmadmin'
}



'''
Test server config
'''
project_config_test = {
    'jmweb':{
        'hosts':['root@47.111.164.172:22'],
        'passwords':['123456'],
        'private_keys':[private_key_path]
    },
    'jmh5':{
        'hosts':['root@47.111.164.172:22'],
        'passwords':['123456'],
        'private_keys':[private_key_path]
    },
    'jmadmin':{
        'hosts':['root@47.111.164.172:22'],
        'passwords':['123456'],
        'private_keys':[private_key_path]
    },
    'jmadmin_h5':{
        'hosts':['root@47.111.164.172:22'],
        'passwords':['123456'],
        'private_keys':[private_key_path]
    },
    'jmpromote':{
        'hosts':['root@47.111.164.172:22'],
        'passwords':['123456'],
        'private_keys':[private_key_path]
    },
    'jmpromote_h5':{
        'hosts':['root@47.111.164.172:22'],
        'passwords':['123456'],
        'private_keys':[private_key_path]
    },
    'gpublish':{
        'hosts':['root@47.111.164.172:22'],
        'passwords':['123456'],
        'private_keys':[private_key_path]
    },
    'publishadmin':{
        'hosts':['root@47.111.164.172:22'],
        'passwords':['123456'],
        'private_keys':[private_key_path]
    },
    'gm_h5_web':{
        'hosts':['root@47.111.164.172:22'],
        'passwords':['123456'],
        'private_keys':[private_key_path]
    },
    'gmapi':{
        'hosts':['root@47.111.164.172:22'],
        'passwords':['123456'],
        'private_keys':[private_key_path]
    },
    'gmadmin':{
        'hosts':['root@47.111.164.172:22'],
        'passwords':['123456'],
        'private_keys':[private_key_path]
    },
    'kwweb':{
        'hosts':['root@47.111.164.172:22'],
        'passwords':['123456'],
        'private_keys':[private_key_path]
    },
    'kwweb_h5':{
        'hosts':['root@47.111.164.172:22'],
        'passwords':['123456'],
        'private_keys':[private_key_path]
    },
    'kwadmin':{
        'hosts':['root@47.111.164.172:22'],
        'passwords':['123456'],
        'private_keys':[private_key_path]
    },
    'kwadmin_h5':{
        'hosts':['root@47.111.164.172:22'],
        'passwords':['123456'],
        'private_keys':[private_key_path]
    },
    'kwpromote':{
        'hosts':['root@47.111.164.172:22'],
        'passwords':['123456'],
        'private_keys':[private_key_path]
    },
    'kwpromote_h5':{
        'hosts':['root@47.111.164.172:22'],
        'passwords':['123456'],
        'private_keys':[private_key_path]
    }
}
project_remote_dir_test = {
    'jmweb':'/data/wwwroot/webgit/jmweb',
    'jmh5':'/data/wwwroot/webgit/jmh5',
    'jmadmin':'/data/wwwroot/webgit/jmadmin',
    'jmadmin_h5':'/data/wwwroot/webgit/jmadmin_h5',
    'jmpromote':'/data/wwwroot/webgit/jmpromote',
    'jmpromote_h5':'/data/wwwroot/webgit/jmpromote_h5',
    'gpublish':'/data/wwwroot/webgit/gpublish',
    'publishadmin':'/data/wwwroot/webgit/publishadmin',
    'gm_h5_web':'/data/wwwroot/webgit/gm_h5_web',
    'gmapi':'/data/wwwroot/webgit/gmapi',
    'gmadmin':'/data/wwwroot/webgit/gmadmin',
    'kwweb':'/data/wwwroot/webgit/kwweb',
    'kwweb_h5':'/data/wwwroot/webgit/kw_h5web',
    'kwadmin':'/data/wwwroot/webgit/kwadmin',
    'kwadmin_h5':'/data/wwwroot/webgit/kw_admin_web',
    'kwpromote':'/data/wwwroot/webgit/kwpromote',
    'kwpromote_h5':'/data/wwwroot/webgit/kw_mailiang_web'
}
project_test_branch_test = {
    'jmweb':'dev',
    'jmh5':'dev',
    'jmadmin':'dev',
    'jmpromote':'dev',
    'gpublish':'dev',
    'publishadmin':'master',
    'gm_h5_web':'master',
    'gmapi':'dev',
    'gmadmin':'dev',
    'kwweb':'dev',
    'kwweb_h5':'master',
    'kwadmin':'master',
    'kwadmin_h5':'master',
    'kwpromote':'master',
    'kwpromote_h5':'master'
}

def web_conn_test(project):
    conn_list = []
    for k in range(len(project_config_test[project]['hosts'])):
        #conn = Connection(project_config[project]['hosts'][k], connect_kwargs={"password": project_config[project]['passwords'][k]})
        try:
            conn = Connection(project_config_test[project]['hosts'][k], connect_kwargs={"key_filename": project_config_test[project]['private_keys'][k]})
        except ValueError as e:
            raise ValueError(e)
        except Exception as e:
            raise Exception(e)
        except:
            raise Exception("unknow error occur !!!")
        conn_list.append(conn)
    return conn_list



@task()
def hello(c,project):

    print "hello fabric",project


def web_conn(project):
    conn_list = []
    for k in range(len(project_config[project]['hosts'])):
        #conn = Connection(project_config[project]['hosts'][k], connect_kwargs={"password": project_config[project]['passwords'][k]})
        try:
            conn = Connection(project_config[project]['hosts'][k], connect_kwargs={"key_filename": project_config[project]['private_keys'][k]})
        except ValueError as e:
            raise ValueError(e)
        except Exception as e:
            raise Exception(e)
        except:
            raise Exception("unknow error occur !!!")
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
def testing(c,project):
    if not project_config_test.has_key(project):
        print("Error: project " + project + " not exist")
        quit()
    try:
        conn_list = web_conn_test(project)
    except ValueError as e:
        print("Error: project " + project + " connect error: "+e)
        quit()
    branch_name = 'dev'
    if project_test_branch_test.has_key(project):
        branch_name = project_test_branch_test[project]
    for conn in conn_list:
        with conn.cd(project_remote_dir_test[project]):
            host = conn.host
            print("The host "+host+" testing begin : "+branch_name)
            try:
                conn.run("git checkout "+branch_name)
                conn.run("git pull ")
            except Exception as e:
                print 'Error: ',e
                quit()
            print("The host "+host+" testing success !!!")
    print("All hosts testing success !!!")

@task
def deploy(c,project):
    if not project_config.has_key(project):
        print("Error: project " + project + " not exist")
        quit()
    tag_list = get_tag_list(c,project)
    tag =  tag_list[-1]
    try:
        conn_list = web_conn(project)
    except ValueError as e:
        print("Error: project " + project + " connect error: "+e)
        quit()
    for conn in conn_list:
        with conn.cd(project_remote_dir[project]):
            host = conn.host
            print("The host "+host+" deploy begin tag: "+tag)
            try:
                conn.run("git fetch origin tag "+tag)
                conn.run("git checkout "+ tag)
            except Exception as e:
                print 'Error: ',e
                quit()
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
    try:
        conn_list = web_conn(project)
    except ValueError as e:
        print("Error: project " + project + " connect error: " + e)
        quit()
    for conn in conn_list:
        with conn.cd(project_remote_dir[project]):
            print("Begin rollback, checkout " + tag)
            try:
                conn.run("git pull",hide=True,warn=True)
                conn.run("git checkout " + tag)
            except Exception as e:
                print 'Error: ',e
                quit()
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