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
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `posts` (
  `post_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `title` text COLLATE utf8mb4_general_ci NOT NULL,
  `tagline` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `slug` varchar(25) COLLATE utf8mb4_general_ci NOT NULL,
  `content` text COLLATE utf8mb4_general_ci NOT NULL,
  `category_id` int DEFAULT NULL,
  `img_file` varchar(20) COLLATE utf8mb4_general_ci DEFAULT 'post-bg.jpg',
  `date` datetime DEFAULT CURRENT_TIMESTAMP,
  `comments_count` int DEFAULT '0',
  `likes_count` int DEFAULT '0',
  `visit_count` int DEFAULT '0',
  PRIMARY KEY (`post_id`),
  KEY `fk_user_id_idx` (`user_id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `posts_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts`
--

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
INSERT INTO `posts` VALUES (1,1,'The Future of Artificial Intelligence','Exploring the Boundary','future-of-ai','Artificial Intelligence (AI) is rapidly evolving, transforming industries and reshaping our daily lives. From self-driving cars to personalized medicine, the potential applications of AI are vast and varied. In this post, we delve into the current advancements in AI, its potential future, and the ethical considerations that come with it.',4,'future_of_ai.jpg','2024-07-28 22:21:41',0,3,65),(2,1,'The Rise of Remote Work','Adapting to the New ','rise-of-remote-work','Remote work has become a significant trend in recent years, accelerated by the global pandemic. Companies are rethinking their office spaces, and employees are adjusting to new work-life balances. This article explores the benefits and challenges of remote work, tips for staying productive, and the future of the workplace.',2,'post-bg.jpg','2024-07-16 22:47:09',1,2,75),(3,1,'Sustainable Living: Tips and Tricks','Making a Difference One Step at a Time','sustainable-living-tips','Sustainability is more important than ever as we face environmental challenges. This blog post provides practical tips and tricks for living a more sustainable lifestyle. From reducing waste to conserving energy, we cover easy-to-implement strategies that can make a big impact on the planet.',3,'sustainable_3.jpg','2024-07-16 22:50:38',0,1,11),(5,2,'Healthy Eating: Myths and Facts','Debunking Common Nutrition Misconceptions','healthy-eating-myths','With so much information available, it\'s easy to get confused about what\'s healthy and what\'s not. This blog post aims to debunk common myths about healthy eating and provide evidence-based facts. Learn about the importance of a balanced diet, the role of different nutrients, and how to make healthier food choices.',3,'sustainable_4.jpg','2024-07-21 15:27:08',1,3,4),(8,5,'The Evolution of Technology in Education','From Chalkboards to Digital Classrooms','tech-in-education','Technology has transformed education, making learning more accessible and engaging. This article explores the evolution of technology in education, from traditional teaching methods to modern digital classrooms. Discover how tools like e-learning platforms, interactive whiteboards, and virtual reality are shaping the future of education.',4,'post-bg.jpg','2024-07-16 22:53:56',0,2,49),(9,5,'Traveling on a Budget: Top Destinations','See the World Without Breaking the Bank','budget-travel-destination','Traveling doesn\'t have to be expensive. With careful planning and smart choices, you can explore amazing destinations on a budget. This blog post highlights some of the best budget-friendly travel destinations around the world. Get tips on how to save money on flights, accommodations, and activities, and make the most of your travel experience.',2,'home-bg.jpg','2024-07-16 23:49:49',1,1,4),(58,23,' Sustainable Living: Simple Changes for a Greener Home','\"Sustainably Yours: Small Changes, Big Impact.\"','sustainable_living','<p>In recent years, the push for sustainable living has gained tremendous momentum. With climate change and environmental degradation becoming increasingly urgent issues, many are looking for ways to live more sustainably. Making simple changes at home can significantly impact the environment while promoting a healthier lifestyle. Here are several effective strategies to create a greener home.</p><h2>Reduce, Reuse, Recycle</h2><p>One of the fundamental principles of sustainable living is the \"three R\'s\": Reduce, Reuse, and Recycle. Start by reducing waste in your home. This can involve consciously purchasing fewer disposable items and opting for products with minimal packaging. For instance, carry a reusable shopping bag when grocery shopping and choose bulk items whenever possible to reduce packaging waste.</p><p>Reusing items extends their life and minimizes waste. Get creative with repurposing old jars as storage containers, or transform worn-out clothing into cleaning rags. Flea markets and online resale platforms can also be great places to find secondhand goods, helping to keep items out of landfills while saving money.</p><p>Recycling is the final step in this process. Familiarize yourself with your local recycling guidelines to ensure you\'re disposing of items correctly. Many communities offer curbside recycling, making it easier to keep recyclables separate from general waste.</p><h2>Embrace Energy Efficiency</h2><p>Improving energy efficiency in your home is another vital step toward sustainability. Simple changes can lead to significant reductions in energy consumption. Start by switching to LED light bulbs, which use up to 80% less energy than traditional incandescent bulbs and last significantly longer.</p><p>Investing in energy-efficient appliances, such as refrigerators, washing machines, and dishwashers, can also reduce your carbon footprint. Look for appliances with the Energy Star label, indicating they meet energy efficiency standards. Additionally, consider unplugging electronics when not in use, as many devices consume energy even in standby mode.</p><p>Another practical approach is to improve your home\'s insulation. Proper insulation helps maintain temperature, reducing the need for heating and cooling systems to work overtime. Weather stripping windows and doors can help prevent drafts, further enhancing energy efficiency.</p><h2>Sustainable Food Choices</h2><p>Your food choices play a crucial role in sustainable living. Opting for local, organic, and seasonal foods can significantly reduce your environmental impact. Local produce doesn’t require long transportation, which reduces carbon emissions. Furthermore, organic farming practices tend to be more environmentally friendly, avoiding synthetic pesticides and fertilizers that can harm the ecosystem.</p><p>Consider starting a small vegetable garden at home. Even a few pots of herbs or vegetables can provide fresh produce and reduce the carbon footprint associated with transporting food. Community gardens are also excellent opportunities to engage with your community while promoting sustainability.</p><h2><strong>Eco-Friendly Products</strong></h2><p>Another way to foster a greener home is to choose eco-friendly products. Many conventional cleaning products contain harmful chemicals that can negatively affect indoor air quality and the environment. Instead, opt for natural cleaning alternatives, such as vinegar, baking soda, and essential oils. These ingredients are not only effective but also safer for your family and pets.</p><p>Similarly, choose sustainable materials for home goods and furnishings. Look for furniture made from reclaimed wood or biodegradable materials, and choose fabrics that are organic or sustainably sourced.</p><h4><br></h4>',3,'sustainable_2.jpg','2024-10-24 16:31:28',0,1,7);
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
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
