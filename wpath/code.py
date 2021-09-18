from __future__ import print_function
from .types import *

# 用来查找调用函数的代码行，方便调试
def findcaller(func):
    """
    查看调用者的文件位置路径和代码调用所在的行数，
    通过这种方式我可以一层一层的追踪代码执行的源头在哪里。
    也就是说一般使用它的场景是理解代码线性处理过程。
    """

    def wrapper(*args, **kwargs):
        import sys

        f = sys._getframe()
        filename = f.f_back.f_code.co_filename
        funcname = f.f_back.f_code.co_name
        lineno = f.f_back.f_lineno

        s_args = "(" + ", ".join([cstr(a) for a in args])
        s_kwargs = [f"{str(d[0])}={cstr(d[1])}" for d in kwargs.items()]
        if s_kwargs:
            s_args += ", " + ", ".join(s_kwargs) + ")"
        else:
            s_args += ")"

        print(
            '\n{}{}\n\tcalled by {} File: "{}", line {}'.format(
                color_y(func.__name__),
                s_args,
                color_y(funcname),
                color_m(filename),
                color_m(lineno),
            )
        )
        return func(*args, **kwargs)

    return wrapper


# 用来查看对象的所有属性和方法
class Atts(object):

    """
    一般用于调试某个对象时使用，当前这个工具类会将调试对象和其所属的所有继承对象的属性依次罗列出来。

    变量 showed_list 它是一个类变量, 用于记录已显示过的对象.

    使用方法:
    Atts.show(调试对象)
    """

    showed_list = []

    @classmethod
    def show(
        cls,  #  cls此处指 Atts
        _class,  # 递归时，传进来的类或对象
        _child_class=None,  # _class的子类
        show_generate=True,  # 打印生成关系
        show_attr=True,  # 打印属性
        show_doc=False,  # 打印文档
        show_parents=False,  # 向上递归打印父类
        show_internal=False,  # 打印内部属性
    ):
        """
        :param _class: 必填, 任意对象.
        :param show_attr: 是否显示_class对象的所有attribute.
        :param show_doc: 是否显示_class对象的__doc__属性.
        :param _child_class: 内部使用的参数, 用来传递_class对象的子类.
        :return:
        """

        def _show(class_name):

            # 如果已经打印过了该类的信息，就不处理
            if class_name in cls.showed_list:
                return
            else:
                # 先将该类添加到已经处理过的列表中
                cls.showed_list.append(class_name)

            # 显示对象和类的继承关系
            if show_generate:
                if _child_class:
                    print(
                        "\n",
                        cstr(class_name),
                        " ==> ",
                        cstr(_child_class),
                    )
                else:
                    print("\n", cstr(class_name))

            if not show_attr:
                return

            for x in dir(class_name):

                if not show_internal:  # 如果不打印内部方法，就不打印__属性__
                    if x.startswith("__") and x.endswith("__"):
                        continue
                try:
                    # 属性变量名
                    attr_name = x
                    # 属性的类型
                    attr_type = type(getattr(class_name, attr_name))
                    # 属性的值
                    attr_object = getattr(class_name, attr_name)

                    print(
                        "\t{!s:<40}: {} =  {}".format(
                            cstr(attr_type, already_typed=True),
                            color_r(attr_name),
                            cstr(attr_object),
                        )
                    )
                except:
                    print("\t{!s:<30} {}".format(cstr(attr_name), "error"))

                if show_doc:
                    if not is_basic_type(attr_object):  # 不打印基础类型的文档
                        doc = getattr(class_name, attr_name).__doc__
                        if doc:  # 如果有文档才打印
                            docs = doc.splitlines()
                            if len(docs) > 5:  # 最多打印5行
                                docs = docs[:5]
                                docs.append("...")
                            doc = "\t\t" + "\n\t\t".join(docs)
                            print(doc)

        # 打印传递进来的类的相关信息
        _show(class_name=_class)

        if show_parents:
            parents = list(getattr(_class, "__bases__", ""))
            parents.append(getattr(_class, "__class__", ""))
            parents = [i for i in parents if i is not object and i is not type and i]

            for i in parents:
                # 递归打印所有的父类
                cls.show(
                    _class=i,
                    _child_class=_class,
                    show_doc=show_doc,
                    show_generate=show_generate,
                    show_attr=show_attr,
                    show_internal=show_internal,
                    show_parents=show_parents,
                )
