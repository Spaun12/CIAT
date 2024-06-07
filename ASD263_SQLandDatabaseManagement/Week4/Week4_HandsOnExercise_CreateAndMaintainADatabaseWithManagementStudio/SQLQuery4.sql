-- Verify the foreign key constraints for the Downloads table
EXEC sp_fkeys @pktable_name = 'Downloads';
