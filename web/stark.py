# -*- encoding: utf-8 -*-
"""
@File    : stark.py
@Time    : 2022/3/1 14:29
@Author  : simon
@Email   : 294168604@qq.com
@Software: PyCharm
"""

from stark.service.v1 import site
from web import models

from web.views.school import SchoolHandler
from web.views.depart import DepartmentHandler
from web.views.userinfo import UserInfoHandler
from web.views.course import CourseHandler
from web.views.classList import ClassListHandler
from web.views.public_customer import PublicCustomerHandler
from web.views.private_customer import PrivateCustomerHandler
from web.views.consult_record import ConsultRecordHandler
from web.views.payment_record import PaymentRecordHandler
from web.views.check_payment_record import CheckPaymentRecordHandler
from web.views.student import StudentHandler
from web.views.score_record import ScoreHandler
from web.views.course_record import CourseRecordHandler



site.register(models.School, SchoolHandler)
site.register(models.Department, DepartmentHandler)
site.register(models.UserInfo, UserInfoHandler)
site.register(models.Course, CourseHandler)
site.register(models.ClassList,ClassListHandler)
site.register(models.Customer,PublicCustomerHandler,'pub')
site.register(models.Customer,PrivateCustomerHandler,'pri')
site.register(models.ConsultRecord,ConsultRecordHandler)
site.register(models.PaymentRecord,PaymentRecordHandler)
site.register(models.PaymentRecord,CheckPaymentRecordHandler,'check')
site.register(models.Student,StudentHandler)
site.register(models.ScoreRecord,ScoreHandler)
site.register(models.CourseRecord,CourseRecordHandler)