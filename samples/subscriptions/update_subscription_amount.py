subscription_service = paymill_context.get_subscription_service();
subscription_without_offer.amount = 5200;
subscription_service.update_with_amount(subscription_without_offer, amount_change_type=1);
