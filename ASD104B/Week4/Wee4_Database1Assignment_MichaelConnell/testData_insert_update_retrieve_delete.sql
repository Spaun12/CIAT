-- 3- Insert test data into Members and Groups tables
INSERT INTO members (memberNAME, memberEmail, memberPhone) 
VALUES ('John Doe', 'john@test.com', '123-456-7890'),
       ('Jane Smith', 'jane@the.com', '987-654-3210'),
       ('Bob Builder', 'bob@code.com', '555-444-3333'),
       ('Alice Wonderland', 'alice@bubba.com', '111-222-3333');

INSERT INTO Groups (groupName, groupDescription) 
VALUES ('Code Cyborg', 'Resistance is futile'),
       ('Keyboard Warriors', 'Masters of the digital realm'),
       ('Bug Busters', 'Somebody has to do it'),
       ('Pixel Pioneers', 'Exploring the, wait, I think we are lost'),
       ('Data Divas', 'Data and Fashion, what more could you want?'),
       ('Git Gurus', 'Com Git some!');

-- 3- Insert test data into MemberGroups table
-- Assign groups to members
-- member_id and group_id start from 1 and increment by 1
INSERT INTO MemberGroups (member_id, group_id) 
VALUES (1, 1),  -- John Doe is in Code Cyborg
       (1, 2),  -- John Doe is also in Keyboard Warriors
       (2, 1),  -- Jane Smith is in Code Cyborg
       (2, 3),  -- Jane Smith is also in Bug Busters
       (3, 4),  -- Bob Builder is in Pixel Pioneers
       (4, 5);  -- Alice Wonderland is in Data Divas

-- 4- Update member's phone number
UPDATE members SET memberPhone = '123-212-3212' WHERE member_id = 1;

-- 5- Retrieve all members
SELECT * FROM members WHERE is_deleted = 0;

-- 6- Soft delete a member
UPDATE members SET is_deleted = 1 WHERE member_id = 1;

-- 7- Retrieve all members that are deleted
SELECT * FROM members WHERE is_deleted = 1;


