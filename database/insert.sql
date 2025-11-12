INSERT INTO contacts (
  phone_number, country_code, display_name, first_name, last_name,
  email, tags, opt_in, opt_in_at, last_contacted_at, is_active
) VALUES (
  '+14155552671',
  'US',
  'Jane Doe',
  'Jane',
  'Doe',
  'jane@example.com',
  ARRAY['marketing','lead']::text[],
  true,
  '2025-11-12T15:00:00Z'::timestamptz,
  NULL,
  true,
)
RETURNING id, created_at, updated_at;