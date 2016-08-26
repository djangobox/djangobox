# 关于: url(r'^mine/$', MyView.as_view(), name='my-view'), 部分的说明

关注django的源码:from django.views.generic import View

类函数Myview.as_view()实际返回的是一个view函数:
as_view():
    def view(request, *args, **kwargs):
        pass

    return view

这个view实际和平时我们在views.py的视图函功能一样的，看看此
函数所带的参数，就清楚了。


特别的地方是，当django调用view函数时，
将会调用：
def dispatch(self, request, *args, **kwargs)[注： 此函数是View对像成员函数]

就是分派的意思，这个函数就做分派任务的工作， 从下面的代码就可以知道:

        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed


比如：request.method.lower() 是 get
那么就会调用：
View 子类里面的get方法，也就是我在views.py函数里面的Myview类里的get方法了，
否则的话，将会调用：http_method_not_allowed 方法
ass MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')



就这样，转一圈回来了。




所以，用户只要实现View子类，并实现对应的方法函数，比如：
get, post等等

整个调用流程是这样：
as_view()-->view()-->dispatch()-->get()或是post()等等，如果找不到对应方法，就调用 http_method_not_allowed

