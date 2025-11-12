INSERT INTO contacts (
  phone_number, display_name, opt_in
) VALUES (
  '+5511999999999',
  'João Silva',
  false
)
RETURNING id, created_at, updated_at;