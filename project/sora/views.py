from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import Customer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CustomerForm


class CustomerList(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'sora/customer_list.html'  # テンプレートのパス
    context_object_name = 'customers'  # テンプレート内で使用する変数名
    paginate_by = 10  # ページネーション（1ページに表示する件数）

    def get_queryset(self):
        """
        クエリセットを取得してソートを適用。
        クエリパラメータ ?sort_by=... に基づいてソート条件を設定します。
        """
        sort_by = self.request.GET.get('sort_by', 'id')  # デフォルトは 'id'
        return Customer.objects.all().order_by(sort_by)

    def get_context_data(self, **kwargs):
        """
        コンテキストデータに現在のソート条件を追加します。
        """
        context = super().get_context_data(**kwargs)
        context['sort_by'] = self.request.GET.get(
            'sort_by', 'id'
        )  # 現在のソート条件
        return context


class DetailCustomer(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'sora/detail_customer.html'


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

    
