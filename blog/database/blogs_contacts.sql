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
-- Table structure for table `contacts`
--

DROP TABLE IF EXISTS `contacts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contacts` (
  `sno` int NOT NULL AUTO_INCREMENT,
  `name` text COLLATE utf8mb4_general_ci NOT NULL,
  `phone_num` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `msg` text COLLATE utf8mb4_general_ci NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `email` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacts`
--

LOCK TABLES `contacts` WRITE;
/*!40000 ALTER TABLE `contacts` DISABLE KEYS */;
INSERT INTO `contacts` VALUES (1,'saksham','111111111','jdwsdiwid','2024-07-11 22:03:38','saksham@gmail.com'),(2,'aman','111','ab toh ho ja','2024-07-12 13:41:27','aman@gmail.com'),(3,'saksham','12','hiii i posting a email','2024-07-12 18:13:56','sakshamagarwal330@gmail.com'),(4,'saksham','1234','ygdekldoipdop','2024-07-12 18:17:33','sakshamagarwal330@gmail.com'),(5,'saksham','1234','ygdekldoipdop','2024-07-12 18:19:39','sakshamagarwal330@gmail.com'),(11,'saksham','111111','hgjkgh;lokijuhygfd','2024-07-12 22:36:00','saksham.singletap@gmail.com'),(16,'utsav singh','9999999999','cswdx','2024-07-13 21:45:25','saksham.singletap@gmail.com'),(17,'sak','1234','ed','2024-07-13 21:45:39','sakshamagarwal330@gmail.com'),(30,'Saksham Agarwal','9660969228','this is final check','2024-09-27 21:36:19','saksham@airforceschooljaipur.edu.in');
/*!40000 ALTER TABLE `contacts` ENABLE KEYS */;
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
