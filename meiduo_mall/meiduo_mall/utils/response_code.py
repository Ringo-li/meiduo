class RETCODE:
    OK                      = "0"
    IMAGECODEERR            = "4001"
    USERERR                 = "4004"

err_msg = {
    RETCODE.OK              : u"成功",
    RETCODE.IMAGECODEERR    : u"图形验证码错误",
    RETCODE.USERERR         : u"用户名错误"


}