#!/usr/bin/env python
# -*- coding:utf-8 -*-

def add_node(tree_dic,comment):
    if comment.parent_comment not in  tree_dic:
        #如果父级不在这层，评论数据就放到这
        tree_dic[comment]={}
    else:#循环当前整个dict，真到找到为止
        for k,v in tree_dic.items():
            if k ==comment.parent_comment:#找到了父级
                tree_dic[comment.parent_comment][comment]={}
            else:#进入下一层继续查找
                add_node(v,comment)

# def render_tree_node(tree_dic,margin_val):
#     html = ""
#     for k,v in tree_dic.items():
#         ele = "<div class='comment-node' style='margin-left:%spx'>" % margin_val + k.comment + "</div>"
#         html += ele
#         html += render_tree_node(v,margin_val+10)
#     return html
#
# def render_comment_tree(tree_dic):
#     html = ""
#     for k,v in tree_dic.items():
#         ele = "<div class='root-comment'>" + k.comment + "</div>"
#         html += ele
#         html += render_tree_node(v,10)
#     return html

def build_tree(comment_set):
    #print(comment_set)
    tree_dic = {}
    for comment in comment_set:
        add_node(tree_dic,comment)

    print('----------')
    for k,v in tree_dic.items():
        print(k,v)
    # return tree_dic