-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: blogs
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `fname` varchar(25) COLLATE utf8mb4_general_ci NOT NULL,
  `lname` varchar(25) COLLATE utf8mb4_general_ci NOT NULL,
  `profile_pic` varchar(45) COLLATE utf8mb4_general_ci DEFAULT 'default-profile-pic.jpg',
  `username` varchar(25) COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `role` varchar(15) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '''subuser''',
  `phone_num` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `email` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `visit_count` int DEFAULT '0',
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  UNIQUE KEY `phone_num_UNIQUE` (`phone_num`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'','','pro.jpg','saksham','$2b$12$V44/0pUgv8kcXvIqJibv3eLcz1t403QMz3GrdFnmPFGDcMOgK6612','admin',NULL,'saksham@gmail.com',0),(2,'sarika','agarwal','default-profile-pic.jpg','sarika1234','hjkl','user','12345678','sarika12345@gmail.com',0),(5,'','','default-profile-pic.jpg','gunnu','qwerty','admin',NULL,'gunnu@gmail.com',0),(12,'','','default-profile-pic.jpg','aman','asdf','user',NULL,'aman@gmail.com',0),(17,'abcd','dfg','default-profile-pic.jpg','saksham123','1234','user','1','sakshamagarwal330@gmail.com',0),(18,'hj','ghj','default-profile-pic.jpg','ghj','r','user','2','a@g.com',0),(20,'h','b','default-profile-pic.jpg','i','$2b$12$F0NXlIAoryNgO/dLR/cQ4.0g6bQj/z3ZsvdBSB/AUp78x4ZIrQwQa','user','3','d@gmail.com',0),(22,'t1','t1','default-profile-pic.jpg','t12','$2b$12$14Dq8wKAiCJzLt9vH4mBI.2a02VSGkYYoBWQrPf2Sr8OKtkrMj8.C','user','44','test1@gmail.com',0),(23,'f','f','default-profile-pic.jpg','h1','$2b$12$V44/0pUgv8kcXvIqJibv3eLcz1t403QMz3GrdFnmPFGDcMOgK6612','user','444','h1@g.com',0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-25  1:14:04
