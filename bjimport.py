#!/usr/bin/python
# -*- coding: utf-8 -*-

import kickerrankade

kickername_rankadename_mapping = {
    u"kangkai":u"尹康凯",
    u"qinling":u"Ling Qin",
    u"Qin ling":u"Ling Qin",
    u"xiaohua":u"Zhaoruihua",
    u"caodan":u"曹先森",
    u"cao dan":u"曹先森",
    u"benchang":u"苏本昌",
    u"xiaoming":u"zhangximing",
    u"suosuo":u"*suosuo",
    u"caolandi":u"*25453678",
    u"cao landi":u"*25453678",
    u"Jia yulong":u"*Jia Yulong",
    u"zhang lei":u"Zhang Lei",
    u"tang meifu":u"*Tang Meifu",
    u"8 hao":u"*8 Hao",
    u"Zhan feng":u"*Zhan Feng",
    u"Xiao tong":u"*Xiao Tong",
    u"Zhao wuji":u"赵无忌",
    u"guangxin":u"*Ren Guangxin"
}

playground = "Black Sun Bar"
groupname = "bjfoosball"

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print "Usage: %s xxx.ktool username passwd" % sys.argv[0]
        print "\t xxx.ktool: file exported from kickertool"
        print "\t username/passwd: your rankade user/pass"
        sys.exit(0)

    kickerrankade.main(sys.argv[1], sys.argv[2], sys.argv[3],
                       playground,
                       groupname,
                       kickername_rankadename_mapping)
