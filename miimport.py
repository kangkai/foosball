#!/usr/bin/python
# -*- coding: utf-8 -*-

import kickerrankade

kickername_rankadename_mapping = {
    u"康凯":u"尹康凯",
    u"尹康凯":u"尹康凯",
    u"孟晓然":u"*Meng Xiaoran",
    u"赵瑞华":u"Zhaoruihua",
    u"曹聃":u"曹先森",
    u"曹凯":u"*Cao Kai",
    u"慧芳":u"*Liu Huifang",
    u"刘慧芳":u"*Liu Huifang",
    u"施磊":u"*Shi Lei",
    u"任恬":u"*Ren Tian",
    u"Ren Tian":u"*Ren Tian",
    u"苏本昌":u"苏本昌",
    u"本昌":u"苏本昌",
    u"肖晓林":u"*Xiao Xiaolin",
    u"国祝":u"*guozhu",
    u"张小武":u"XiaowuZhang",
    u"韩广义":u"HanGuangyi",
    u"广义":u"HanGuangyi",
    u"Matt":u"*matt",
    u"张茜明":u"zhangximing",
    u"茜明":u"zhangximing",
    u"博士":u"*boshi",
    u"鑫岩":u"Xinyan Xing",
    u"邢鑫岩":u"Xinyan Xing",
    u"Lisa":u"*Lisa",
    u"lisa":u"*Lisa",
    u"关剑喜（替补）":u"*guanjianxi",
    u"彭亚":u"*Peng Ya",
    u"Peng Ya":u"*Peng Ya",
    u"教练":u"*Gu Yafei",
    u"Yu Yunda":u"*Yu Yunda",
    u"于运达":u"*Yu Yunda",
    u"高飞":u"*Gao Fei",
    u"lily":u"Lilyhao",
    u"秦岭":u"Ling Qin",
    u"陶见涛":u"*Tao Jiantao",
    u"米思远":u"*Mi Siyuan",
    u"雷霞":u"*Lei Xia",
    u"佐罗":u"*Zuo Luo"
}

playground = "Xiaomi Wuchaicheng 11F"
groupname = "mifoosball"

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
