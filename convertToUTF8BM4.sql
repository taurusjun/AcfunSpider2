ALTER TABLE actest2.accomment CONVERT TO CHARACTER SET utf8mb4;
ALTER TABLE actest2.accomment MODIFY content Text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE actest2.accomment MODIFY userName varchar(120) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE actest2.accomment MODIFY userImg varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE actest2.accomment MODIFY verifiedText Text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE actest2.accommentcache CONVERT TO CHARACTER SET utf8mb4;
ALTER TABLE actest2.accommentcache MODIFY content Text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE actest2.accommentcache MODIFY userName varchar(120) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE actest2.accommentcache MODIFY userImg varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE actest2.accommentcache MODIFY verifiedText Text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
