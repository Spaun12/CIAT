-- Michael Connell 2023-09-24
-- Task 1: Create the Members table with respective columns, data types, and enhancements
CREATE TABLE members (
    member_id INT(11) AUTO_INCREMENT PRIMARY KEY,
    memberNAME VARCHAR(50) NOT NULL,
    memberEmail VARCHAR(50) UNIQUE NOT NULL,
    memberPhone VARCHAR(15),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    is_deleted BOOLEAN DEFAULT 0
);

-- Task 1: Create the Groups table with respective columns, data types, and enhancements
CREATE TABLE Groups (
    group_id INT(11) AUTO_INCREMENT PRIMARY KEY,
    groupName VARCHAR(50) NOT NULL,
    groupDescription TEXT,
    status ENUM('Active', 'Inactive') DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    is_deleted BOOLEAN DEFAULT 0
);
