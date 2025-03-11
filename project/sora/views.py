from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Customer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CustomerForm
from io import BytesIO
from barcode import Code39
from barcode.writer import SVGWriter

class CustomerList(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'sora/customer_list.html'  # テンプレートのパス
    context_object_name = 'customers'  # テンプレート内で使用する変数名

    def get_queryset(self, **kwargs):
        """
        クエリセットを取得してソートを適用。
        クエリパラメータ ?sort_by=... に基づいてソート条件を設定します。
        """
        queryset = super().get_queryset(**kwargs)
        print(f'くえり：{ queryset }')
        sort_by = self.request.GET.get('sort_by', 'id')  # デフォルトは 'id'
        return Customer.objects.all().order_by(sort_by)

    def get_context_data(self, **kwargs):
        """
        コンテキストデータに現在のソート条件を追加します。
        """
        context = super().get_context_data(**kwargs)
        print(f'コンテキスト: {context}')
        context['sort_by'] = self.request.GET.get(
            'sort_by', 'id'
        )  # 現在のソート条件
        return context


class DetailCustomer(LoginRequiredMixin, DetailView):
    model = Customer
    print(model)
    template_name = 'sora/detail_customer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = Customer.objects.get(id=self.kwargs['pk'])  # ✅ `self.kwargs['pk']` で取得

        rv = BytesIO()
        barcode = Code39(str(customer.id), writer=SVGWriter()).write(rv)
        barcode_svg = rv.getvalue().decode()

        print("=== Debug: Generated Barcode SVG ===")
        print(barcode_svg)  # ✅ SVG データを確認
        print("===============================")
        print(barcode)

        context['barcode'] = barcode_svg
        return context  # ✅ `rend

    # def get_context_data(self, ):
    #     rv = BytesIO()
    #     customer = self.get_object()
    #     barcode = Code39(str(customer.id), writer=SVGWriter()).write(rv)
    #     barcode_svg = rv.getvalue().decode()

    #     # 確認用に出力
    #     print("=== Debug: Generated Barcode SVG ===")
    #     print(barcode_svg)  # SVG データを確認
    #     print("===============================")
    #     print(barcode)
    #     context = {'barcode': barcode_svg}
    #     return render(request, "sora/detail_customer.html", context)


class CreateCustomer(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'sora/customer_create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        print('success_url:',self.get_success_url())

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('sora:detail_customer', args=[self.object.pk])

    
def generate_barcode(request, pk):
    rv = BytesIO()
    customer = Customer.objects.get(id=pk)
    barcode = Code39(str(customer.id), writer=SVGWriter()).write(rv)
    barcode_svg = rv.getvalue().decode()

    context = {'barcode': barcode_svg}
    return render(request, "sora/detail_customer.html", context)


class UpdateCustomer(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'sora/customer_update.html'
    
    def get_success_url(self):
        return reverse_lazy('sora:detail_customer',kwargs={'pk':self.object.pk})
    

class DeleteCustomer(DeleteView):
    model = Customer
    success_url = reverse_lazy('sora:index')