# -*- encoding: utf-8 -*-
"""
@File    : base.py
@Time    : 2022/3/13 21:22
@Author  : simon
@Email   : 294168604@qq.com
@Software: PyCharm
"""
class PermissionHandler(object):
    #根据权限控制按钮
    # 是否显示添加按钮
    def get_add_btn(self, request, *args, **kwargs):
        from django.conf import settings
        # 当前用户所有的权限信息
        permission_dict = request.session.get(settings.PERMISSION_SESSION_KEY)
        if self.get_add_url_name not in permission_dict:
            return None
        return super().get_add_btn(request, *args, **kwargs)

    # 是否显示编辑和删除按钮
    def get_list_display(self, request, *args, **kwargs):
        from django.conf import settings
        # 当前用户所有的权限信息
        permission_dict = request.session.get(settings.PERMISSION_SESSION_KEY)
        value = []
        if self.list_display:
            value.extend(self.list_display)
            if self.get_change_url_name in permission_dict and self.get_delete_url_name in permission_dict:
                value.append(type(self).display_edit_del)
            elif self.get_change_url_name in permission_dict:
                value.append(type(self).display_edit)
            elif self.get_delete_url_name in permission_dict:
                value.append(type(self).display_del)
        return value
