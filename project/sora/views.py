from django.views.generic import ListView, DetailView
from .models import Customer

class CustomerList(ListView):
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
        context['sort_by'] = self.request.GET.get('sort_by', 'id')  # 現在のソート条件
        return context
    
class DetailCustomer(DetailView):
    model = Customer
    template_name = 'sora/detail_customer.html'

