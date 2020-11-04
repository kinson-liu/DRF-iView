from rest_framework.exceptions import APIException
from rest_framework import status
# 自定义异常分类
class AuthenticationFailed(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_code = 10001
    default_detail = 'Token认证失败'

class LoginFailed(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = 11000
    default_detail = '登录失败，用户名或密码错误'

class UserNotExist(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = 11001
    default_detail = '获取用户信息失败，无法找到此用户'

class BusinessException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = '业务异常'
class SystemException(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_code = '系统异常'

class ParameterException(BusinessException):
    default_code = '参数错误'
class DatabaseException(BusinessException):
    default_code =  '数据库错误'
