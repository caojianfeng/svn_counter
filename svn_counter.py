#!/usr/bin/env python
# coding=utf8
__author__ = 'caojianfeng'
import sys, os


# java -jar ../statsvn.jar ../nova/日志名XXX.log ../nova  -charset utf-8 -disable-twitter-button -title Nova  -include **/*.cpp:**/*.h -exclude **/sqlite3/*.*

def count_svn(project_path):
    cmd_path = os.path.abspath(os.curdir)
    project_parent, poject_dir_name = os.path.split(project_path)
    output_path = cmd_path + "/output_%s" % poject_dir_name
    print os.path.abspath(os.curdir)
    cmds = ["svn update %s" % project_path, "svn log %s --xml -v > %s/svn.log" % (project_path, cmd_path),
            "java -jar %s/statsvn.jar %s/svn.log %s  -output-dir %s -charset utf-8 -disable-twitter-button -title %s  -include **/*.cpp:**/*.h:**/*.java:**/*.xml:**/*.m -exclude **/sqlite3/*.*" % (
                cmd_path, cmd_path, project_path, output_path, poject_dir_name)
            ]
    for cmd in cmds:
        print cmd
        os.system(cmd)
    os.chdir(cmd_path)


def show_using():
    print "python svn_counter.py project_dir"


# -- main ---
if __name__ == '__main__':
    print sys.argv
    if len(sys.argv) > 1:
        project_dir = sys.argv[1]
        count_svn(project_dir)
    else:
        show_using()
