-- MySQL dump 10.13  Distrib 5.7.19, for osx10.12 (x86_64)
--
-- Host: localhost    Database: actest2
-- ------------------------------------------------------
-- Server version	5.7.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE DATABASE `actest2` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `actest2`;

--
-- Table structure for table `accomment`
--

DROP TABLE IF EXISTS `accomment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accomment` (
  `cid` bigint(20) NOT NULL AUTO_INCREMENT,
  `acid` bigint(20) DEFAULT NULL,
  `quoteId` bigint(20) DEFAULT NULL,
  `content` text,
  `postDate` datetime DEFAULT NULL,
  `userID` bigint(20) DEFAULT NULL,
  `userName` varchar(120) DEFAULT NULL,
  `userImg` varchar(300) DEFAULT NULL,
  `localImgPath` varchar(300) DEFAULT NULL,
  `count` int(11) DEFAULT NULL,
  `deep` int(11) DEFAULT NULL,
  `isSignedUpCollege` tinyint(1) DEFAULT NULL,
  `refCount` int(11) DEFAULT NULL,
  `ups` int(11) DEFAULT NULL,
  `downs` int(11) DEFAULT NULL,
  `nameRed` int(11) DEFAULT NULL,
  `avatarFrame` int(11) DEFAULT NULL,
  `isDelete` tinyint(1) DEFAULT NULL,
  `isUpDelete` tinyint(1) DEFAULT NULL,
  `nameType` int(11) DEFAULT NULL,
  `verified` int(11) DEFAULT NULL,
  `verifiedText` text,
  `updateDate` datetime DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=84069752 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `accommentImg`
--

DROP TABLE IF EXISTS `accommentImg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accommentImg` (
  `cid` bigint(20) NOT NULL AUTO_INCREMENT,
  `acid` bigint(20) DEFAULT NULL,
  `quoteId` bigint(20) DEFAULT NULL,
  `content` text,
  `postDate` datetime DEFAULT NULL,
  `userID` bigint(20) DEFAULT NULL,
  `userName` varchar(30) DEFAULT NULL,
  `userImg` varchar(120) DEFAULT NULL,
  `localImgPath` varchar(300) DEFAULT NULL,
  `count` int(11) DEFAULT NULL,
  `deep` int(11) DEFAULT NULL,
  `isSignedUpCollege` tinyint(1) DEFAULT NULL,
  `refCount` int(11) DEFAULT NULL,
  `ups` int(11) DEFAULT NULL,
  `downs` int(11) DEFAULT NULL,
  `nameRed` int(11) DEFAULT NULL,
  `avatarFrame` int(11) DEFAULT NULL,
  `isDelete` tinyint(1) DEFAULT NULL,
  `isUpDelete` tinyint(1) DEFAULT NULL,
  `nameType` int(11) DEFAULT NULL,
  `verified` int(11) DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=81301684 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `accommentcache`
--

DROP TABLE IF EXISTS `accommentcache`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accommentcache` (
  `cid` bigint(20) NOT NULL AUTO_INCREMENT,
  `acid` bigint(20) DEFAULT NULL,
  `quoteId` bigint(20) DEFAULT NULL,
  `content` text,
  `postDate` datetime DEFAULT NULL,
  `userID` bigint(20) DEFAULT NULL,
  `userName` varchar(120) DEFAULT NULL,
  `userImg` varchar(300) DEFAULT NULL,
  `localImgPath` varchar(300) DEFAULT NULL,
  `count` int(11) DEFAULT NULL,
  `deep` int(11) DEFAULT NULL,
  `isSignedUpCollege` tinyint(1) DEFAULT NULL,
  `refCount` int(11) DEFAULT NULL,
  `ups` int(11) DEFAULT NULL,
  `downs` int(11) DEFAULT NULL,
  `nameRed` int(11) DEFAULT NULL,
  `avatarFrame` int(11) DEFAULT NULL,
  `isDelete` tinyint(1) DEFAULT NULL,
  `isUpDelete` tinyint(1) DEFAULT NULL,
  `nameType` int(11) DEFAULT NULL,
  `verified` int(11) DEFAULT NULL,
  `verifiedText` text,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=84071291 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-07-31 11:03:03
