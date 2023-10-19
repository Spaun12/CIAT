-- Michael Connell 2023-09-24
-- Enhancement: Add an index on memberEmail for faster search
CREATE INDEX idx_memberEmail ON members(memberEmail);
