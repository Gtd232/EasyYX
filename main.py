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


dl1 = ['{}大家好，这里是{}，接下来小编跟大家了解一下{}。那么{}到底是什么呢？接下来一起来跟小编了解一下{}吧！\n\n'.format(Reader, Writer, Thing, Thing, Thing),
       'Hello，{}大家好，欢迎收看本期的{}，{}可以点击订阅关注我们，喜欢的话记得留言收藏和点赞哦。接下来小编跟大家来了解一下{}。那么{}到底是什么呢？接下来一起来跟小编了解一下{}吧！\n\n'.format(Reader, Writer, Reader, Thing, Thing, Thing),
       '{}大家好，我是{}，快点订阅关注！必须点赞留言收藏！不然我就不写文章了！唔唔唔！今天来了解了解一下{}，快点给我来了解{}！\n\n'.format(Reader, Writer, Reader, Thing, Thing)]

dl2 = ['{}，众所周知，{}是就是{}，那么这是为什么呢？有专家说这是金科玉律，{}是不是很神奇呢？\n\n'.format(Reader, Thing, Thing2, Thing),
       '{}，近日，一位外国小哥发现了{}，小哥首先吸了一口气，可以看到他还呼出一口气了，这还真是神奇呢，不得不说老外的思维很开阔了。\n\n'.format(Reader, Thing),
       '说起{}，相信大家一定很熟悉，但{}是什么呢？就让小编带大家一起了解吧！其实，{}就是{}，大家可能会惊讶，{}竟然就是{}！那到底为什么{}就是{}呢？其实小编也不是很理解！\n\n'.format(Thing, Thing, Thing, Thing2, Thing, Thing2, Thing, Thing2),
       '{}一定很熟悉{}，{}就是{}！{}就是{}！\n\n'.format(Reader, Thing, Thing, Thing2, Thing, Thing2)]

dl3 =['这就是{}了，不知道大家有什么想法呢？欢迎在屏幕下方留言哦！最后小编跟大家玩个游戏：{}+{} = ？知道的{}可以打在评论区哦！\n\n'.format(Thing, randint(1, 10), randint(1, 10), Reader),
      '{}，这就是{}了，不知道大家有什么想法呢？欢迎在屏幕下方留言哦！\n\n'.format(Reader, Thing),
      '好了，本期文章就到这啦，喜欢的{}可以点击订阅收藏和关注，我们下期再见，拜拜。\n\n'.format(Reader),
      '这就是{}！快点订阅关注！必须点赞留言收藏！不然我就不写文章了！唔唔唔！下期再见，下期再见！唔唔唔！\n\n'.format(Thing)]

wz = choice(dl1) + choice(dl2) + choice(dl3)

print((wz))
