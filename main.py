# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Gtd232

# ”听君一席话，白读十年书”系列
# 哦对，这是废话令，不是飞花令

# 大家以后不被这些垃圾文章浪费时间


from random import randint, choice
Reader = '小伙伴们'
Writer = 'XX看XX'
Thing = '李尚学校'
Thing2 = '花溪建的学校'


dl1 = [
    f'{Reader}大家好，这里是{Writer}，接下来小编跟大家了解一下{Thing}。那么{Thing}到底是什么呢？接下来一起来跟小编了解一下{Thing}吧！\n\n',
    f'Hello，{Reader}大家好，欢迎收看本期的{Writer}，{Reader}可以点击订阅关注我们，喜欢的话记得留言收藏和点赞哦。接下来小编跟大家来了解一下{Thing}。那么{Thing}到底是什么呢？接下来一起来跟小编了解一下{Thing}吧！\n\n',
    f'{Reader}大家好，我是{Writer}，快点订阅关注！必须点赞留言收藏！不然我就不写文章了！唔唔唔！今天来了解一下{Reader}，快点给我来了解{Thing}！\n\n',
]

dl2 = [
    f'{Reader}，众所周知，{Thing}是就是{Thing2}，那么这是为什么呢？有专家说这是金科玉律，{Thing}是不是很神奇呢？\n\n',
    f'{Reader}，近日，一位外国小哥发现了{Thing}，小哥首先吸了一口气，可以看到他还呼出一口气了，这还真是神奇呢，不得不说老外的思维很开阔了。\n\n',
    f'说起{Thing}，相信大家一定很熟悉，但{Thing}是什么呢？就让小编带大家一起了解吧！其实，{Thing}就是{Thing2}，大家可能会惊讶，{Thing}竟然就是{Thing2}！那到底为什么{Thing}就是{Thing2}呢？其实小编也不是很理解！\n\n',
    f'{Reader}一定很熟悉{Thing}，{Thing}就是{Thing2}！{Thing}就是{Thing2}！\n\n',
]

dl3 = [
    f'这就是{Thing}了，不知道大家有什么想法呢？欢迎在屏幕下方留言哦！最后小编跟大家玩个游戏：{randint(1, 10)}+{randint(1, 10)} = ？知道的{Reader}可以打在评论区哦！\n\n',
    f'{Reader}，这就是{Thing}了，不知道大家有什么想法呢？欢迎在屏幕下方留言哦！\n\n',
    f'好了，本期文章就到这啦，喜欢的{Reader}可以点击订阅收藏和关注，我们下期再见，拜拜。\n\n',
    f'这就是{Thing}！快点订阅关注！必须点赞留言收藏！不然我就不写文章了！唔唔唔！下期再见，下期再见！唔唔唔！\n\n',
]

wz = choice(dl1) + choice(dl2) + choice(dl3)

print((wz))
