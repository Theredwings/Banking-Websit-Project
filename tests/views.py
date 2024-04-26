from django.shortcuts import render, redirect
from tests.models import savingaccount

from django.contrib.auth.decorators import login_required
import random
from django.views import View
from django.contrib.auth.hashers import make_password, check_password
import os


# Create your views here.
def home(request):
    mess = 0
    mas = 0
    if request.method == "POST":
        ak = request.FILES

        if len(request.POST["acount"]) > 0:
            x = savingaccount.objects.all()

            f = 0

            if len(x) > 0:
                for i in x:
                    if i.addhar_number == int(request.POST["adhar"]):
                        f = f + 1
                        break
            if request.POST["npass"] != request.POST["cpass"]:
                return render(
                    request,
                    "templates/home.html",
                    {"msg": "Please enter same password"},
                )

            elif f >= 1:
                return render(
                    request,
                    "templates/home.html",
                    {"msg": "User alredy exist, try to login "},
                )
            elif len(request.POST["adhar"]) == 12 and len(request.POST["phoe"]) == 10:
                acc_no = 0
                while True:
                    acc_no = random.randint(100000000000, 999999999999)
                    a = []
                    if len(x) > 0:
                        for i in x:
                            a.append(i.a_number)

                    break
                if acc_no not in a:
                    pas = make_password(request.POST["cpass"])

                    n = savingaccount(
                        name=request.POST["name"],
                        email=request.POST["emai"],
                        mobile_number=request.POST["phoe"],
                        addhar_number=request.POST["adhar"],
                        password=pas,
                        Account_type=request.POST["acount"],
                        ocupation=request.POST["sel"],
                        a_number=acc_no,
                        salary=0,
                        loan=0,
                        image=ak["ph"],
                    )
                    n.save()

                    return render(
                        request,
                        "templates/account.html",
                        {
                            "name": request.POST["name"],
                            "email": request.POST["emai"],
                            "phone": request.POST["phoe"],
                            "acc": acc_no,
                            "adh": request.POST["adhar"],
                        },
                    )
    try:

        if request.COOKIES["acc"]:
            b = savingaccount.objects.get(a_number=request.COOKIES["acc"])
            return render(request, "templates/home.html", {'dat':b})
    except:
        pass
    
    return render(request, "templates/home.html", {"mess": mess, "mas": mas })


def presnoaloan(request):
    fin = 0
    year = 0
    if request.method == "POST":

        year = request.POST["rang"]
        amount = request.POST["loan"]
        fin = ((int(amount) * 14) / 100) * int(year) + int(amount)
    
    try:

        if request.COOKIES["acc"]:
            b = savingaccount.objects.get(a_number=request.COOKIES["acc"])
            return render(request, "templates/loan.html", {'dat':b})
    except:
        pass

    return render(request, "templates/Loan.html", {"yr": year, "final": fin})


def apply(request):
    if request.method == "POST":
        name = request.POST["name"]
        adhar = request.POST["anumber"]
        age = request.POST["age"]
        ocup = request.POST["sel"]
        sal = request.POST["sal"]
        print(type(adhar), type(int(sal)), int(sal))
        try:
            if (
                len(request.POST["anumber"]) == 12
                and len(request.POST["pnumber"]) == 10
            ):
                n = savingaccount.objects.get(addhar_number=adhar)
                if (
                    name == n.name
                    and adhar == n.addhar_number
                    and n.mobile_number == request.POST["pnumber"]
                ):

                    pass

        except:
            print("sorry you are not my customer! ")
        else:
            try:
                if int(sal) >= 150000 and (int(age) >= 21 and int(age) < 61):
                    print(n.salary)
                    n.salary = n.salary + int(request.POST["lm"])
                    n.loan = n.loan - int(request.POST["lm"])

                    n.save()
                    return redirect("/apply", {"ap": name})
            except:
                print("you are not elegible for loan")
    try:

        if request.COOKIES["acc"]:
            b = savingaccount.objects.get(a_number=request.COOKIES["acc"])
            return render(request, "templates/apply.html", {'dat':b})
    except:
        pass

    return render(request, "templates/apply.html")


class login(View):
    def get(self, request):
        return render(request, "templates/login.html")

    def post(self, request):
        x = savingaccount.objects.get(mobile_number=int(request.POST["user"]))
        if x != None:

            if check_password(request.POST["pass"], x.password) == True:
                res = render(request,"templates/home.html",{'dat':x})
                res.set_cookie("acc", x.a_number)
                res.set_cookie("ima", x.image.url)
                res.set_cookie("nae", x.name)
                return res
            else:
                return render(
                    request, "templates/login.html", {"m": "invalid password"}
                )
        else:
            mas = "invalid phone no and password"
            return render(request, "templates/login.html", {"mas": mas})


class about(View):
    def get(self, request):
        try:

            if request.COOKIES["acc"]:
                b = savingaccount.objects.get(a_number=request.COOKIES["acc"])
                return render(request, "templates/about.html", {'dat':b})
        except:
            pass
        return render(request, "templates/about.html")


def banktranfer(request):
    if request.method == "POST":
        try:
            a = request.COOKIES["acc"]
        except:
            return redirect("/login")
        else:
            a = savingaccount.objects.get(a_number=int(request.POST["ac"]))

            if a != None:
                if a.name == request.POST["name"] and a.mobile_number == int(
                    request.POST["phoe"]
                ):
                    c = savingaccount.objects.get(a_number=int(request.COOKIES["acc"]))
                    if c != None:
                        if c.salary >= int(request.POST["amt"]):
                            c.salary = c.salary - int(request.POST["amt"])
                            a.salary += int(request.POST["amt"])
                            a.save()
                            c.save()
                        else:
                            mas = "insufficiant balance"
                            return render(
                                request, "templates/banktrans.html", {"ma": mas}
                            )
                else:
                    mas = "Please enter correct name and number"
                    return render(request, "templates/banktrans.html", {"ma": mas})
            else:
                mas = "invalid user"
                return render(request, "templates/banktrans.html", {"ma": mas})
    return render(request, "templates/banktrans.html")


def deposit(request):
    if request.method == "POST":
        try:
            a = request.COOKIES["acc"]
        except:
            return redirect("/login")
        else:
            a = savingaccount.objects.get(mobile_number=int(request.POST["phoe"]))

            if a != None:
                if a.name == request.POST["name"] and a.mobile_number == int(
                    request.POST["phoe"]
                ):
                    c = savingaccount.objects.get(a_number=int(request.COOKIES["acc"]))
                    if c != None:
                        c.salary += int(request.POST["amt"]) * 2

                        c.save()

                else:
                    mas = "Please enter correct name and number"
                    return render(request, "templates/banktrans.html", {"ma": mas})
            else:
                mas = "invalid user"
                return render(request, "templates/banktrans.html", {"ma": mas})
    return render(request, "templates/deposit.html")


def logout(request):
    res = redirect("/")
    res.delete_cookie("acc")
    res.delete_cookie("ima")
    return res


def edit(request):
    if request.method == "POST":
        a = request.FILES
        b = savingaccount.objects.get(a_number=request.COOKIES["acc"])
        l = b.image
        os.remove(f"D:\\django practice\\temp\\media\\{l}")
        b.image = a["imgs"]
        b.email = request.POST["em"]
        b.save()
        x=savingaccount.objects.get(a_number=request.COOKIES["acc"])
        return render(request,"templates/edit.html",{'dat':x , "em": x.email ,"nm": x.name})
    b = savingaccount.objects.get(a_number=request.COOKIES["acc"])
    return render(request, "templates/edit.html", {"em": b.email,'dat':b ,"nm": b.name})
