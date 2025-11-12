CREATE EXTENSION IF NOT EXISTS "pgcrypto";

CREATE TABLE IF NOT EXISTS contacts (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  phone_number text NOT NULL,             -- E.164 format recommended (+1234567890)
  country_code text,                      -- e.g. "US", "BR" or numeric country calling code
  display_name text,
  first_name text,
  last_name text,
  email text,
  tags text[] DEFAULT ARRAY[]::text[],    -- simple tags/labels
  opt_in boolean DEFAULT false,           -- whether they gave consent to be messaged
  opt_in_at timestamptz,
  last_contacted_at timestamptz,
  is_active boolean DEFAULT true,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);

-- Prevent duplicate phone numbers
CREATE UNIQUE INDEX IF NOT EXISTS contacts_phone_number_idx ON contacts (phone_number);

-- Optional index for tags if you query by tag
CREATE INDEX IF NOT EXISTS contacts_tags_gin_idx ON contacts USING gin (tags);

-- Trigger to keep updated_at current
CREATE OR REPLACE FUNCTION handle_updated_at()
RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN
  NEW.updated_at = now();
  RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS contacts_updated_at_trig ON contacts;
CREATE TRIGGER contacts_updated_at_trig
BEFORE UPDATE ON contacts
FOR EACH ROW EXECUTE FUNCTION handle_updated_at();