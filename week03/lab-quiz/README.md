| Unit Price (TRY) | Stock | Requested Qty | Subtotal (TRY) | Member? | Expected Status | Expected Final Price |
|---|---|---|---|---|---|---|
| 100.0 | 10 | 4 | 400.0 (Just below) | yes | Approved (Standard) | 400.00 TRY |
| 100.0 | 10 | 5 | 500.0 (Exactly at) | yes | Approved (10% Discount) | 450.00 TRY |
| 100.0 | 10 | 6 | 600.0 (Above) | yes | Approved (10% Discount) | 540.00 TRY |

Test Ran: Tested with `unit_price = 100`, `quantity = 5`, `is_member = yes` (subtotal = 500 TRY).
Change Made: Initially used `subtotal > 500` for the discount rule, which failed the boundary check at exactly 500 TRY. Changed the comparison operator to `subtotal >= 500` to correctly include 500 TRY in the discount policy.
