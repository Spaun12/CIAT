-- Michael Connell 2023-09-24
-- Create the junction table to handle the many-to-many relationship
CREATE TABLE MemberGroups (
    member_group_id INT(11) AUTO_INCREMENT PRIMARY KEY,
    member_id INT(11),
    group_id INT(11),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    is_deleted BOOLEAN DEFAULT 0,
    FOREIGN KEY (member_id) REFERENCES members(member_id),
    FOREIGN KEY (group_id) REFERENCES Groups(group_id)
);
