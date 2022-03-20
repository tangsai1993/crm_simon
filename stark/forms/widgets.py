# -*- encoding: utf-8 -*-
"""
@File    : widgets.py
@Time    : 2022/3/6 15:52
@Author  : simon
@Email   : 294168604@qq.com
@Software: PyCharm
"""
from django import forms


class DateTimePickerInput(forms.TextInput):
    template_name = 'stark/forms/widgets/datetime_picker.html'