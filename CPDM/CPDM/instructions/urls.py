from django.urls import path

from CPDM.instructions.views import CreateInstructionView, ListInstructionsView, DetailsInstructionView, \
    UpdateInstructionView, DeleteInstructionView

urlpatterns = (
    path('create/', CreateInstructionView.as_view(), name='instruction_create'),
    path('list/', ListInstructionsView.as_view(), name='instructions_list'),
    path('details/<int:instruction_id>/', DetailsInstructionView.as_view(), name='instruction_details'),
    path('update/<int:instruction_id>/', UpdateInstructionView.as_view(), name='update_instruction'),
    path('delete/<int:instruction_id>/', DeleteInstructionView.as_view(), name='delete_instruction'),
)
