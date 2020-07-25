/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.9 : Database - prediction
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`prediction` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `prediction`;

/*Table structure for table `company` */

DROP TABLE IF EXISTS `company`;

CREATE TABLE `company` (
  `company_id` int(11) NOT NULL AUTO_INCREMENT,
  `log_id` int(11) DEFAULT NULL,
  `companyname` varchar(100) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `phoneno` varchar(15) DEFAULT NULL,
  `emailid` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `company` */

insert  into `company`(`company_id`,`log_id`,`companyname`,`address`,`phoneno`,`emailid`) values (5,14,'riss tech','ernakulam south','999555661','risstech@gmail'),(6,16,'info','kottayam','9876543210','info@gmail'),(7,17,'info','ernakulam','999555661','info@gmail.com');

/*Table structure for table `course` */

DROP TABLE IF EXISTS `course`;

CREATE TABLE `course` (
  `course_id` int(11) NOT NULL AUTO_INCREMENT,
  `coursename` varchar(50) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `course` */

insert  into `course`(`course_id`,`coursename`,`description`) values (2,'BCA','Bachelor of Computer Applications');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`log_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`log_id`,`username`,`password`,`type`) values (1,'admin','admin','admin'),(10,'biny','12345','staff'),(14,'riss','0007','company'),(17,'info','0000','company'),(18,'ameen','0101','staff');

/*Table structure for table `selection` */

DROP TABLE IF EXISTS `selection`;

CREATE TABLE `selection` (
  `select_id` int(11) NOT NULL AUTO_INCREMENT,
  `company_id` int(11) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `predicted` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`select_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `selection` */

insert  into `selection`(`select_id`,`company_id`,`student_id`,`date`,`predicted`) values (3,7,4,'2020-03-04','90.44187240708452'),(4,7,1,'2020-03-04','0.04013300614951276');

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `log_id` int(11) DEFAULT NULL,
  `firstname` varchar(50) DEFAULT NULL,
  `lastname` varchar(50) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `designation` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `qualification` varchar(50) DEFAULT NULL,
  `phoneno` varchar(15) DEFAULT NULL,
  `emailid` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`log_id`,`firstname`,`lastname`,`dob`,`designation`,`place`,`qualification`,`phoneno`,`emailid`) values (3,13,'Binyamin','Abbas','2020-01-15','clerk','mvpa','MCA','12345489798','binyamin@gmail'),(4,18,'Ameen','Abbas','2020-01-09','Accountant','Vannapuram','Bsc','9854762321','ameenp@gmail.com');

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `student_id` int(11) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(50) DEFAULT NULL,
  `lastname` varchar(50) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `phoneno` varchar(15) DEFAULT NULL,
  `emailid` varchar(50) DEFAULT NULL,
  `housename` varchar(25) DEFAULT NULL,
  `place` varchar(30) DEFAULT NULL,
  `pincode` varchar(10) DEFAULT NULL,
  `guardianname` varchar(50) DEFAULT NULL,
  `relationship` varchar(20) DEFAULT NULL,
  `guardianphone` varchar(15) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `interest` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `student` */

insert  into `student`(`student_id`,`firstname`,`lastname`,`dob`,`gender`,`phoneno`,`emailid`,`housename`,`place`,`pincode`,`guardianname`,`relationship`,`guardianphone`,`course_id`,`interest`) values (1,'Binyamin','Abbas','2020-01-10','male','9995916232','binyamin@gmail','PAZHAYARIYIL','dmvpa','685607','Abbas','father','82525252',2,'Skills'),(3,'asdgdfgdf','wewre','2020-01-08','male','654646513213','fghkjhkgkghgk','PAZHAYARIYIL','dfsdfgf','685607','gskjhsdfkjsgdhf','father','35486484',1,'aaaaa'),(4,'ameen','Abbas','2020-01-02','male','9995916232','ameen@gmail.com','pazhery','vpm','665588','Abbas','father','8889991999',2,'jhfljkhsdfljhsda;');

/*Table structure for table `tbl_criteria` */

DROP TABLE IF EXISTS `tbl_criteria`;

CREATE TABLE `tbl_criteria` (
  `criteria_id` int(10) NOT NULL AUTO_INCREMENT,
  `criteria_name` varchar(20) NOT NULL,
  `criteria_level_range` varchar(40) NOT NULL,
  `criteria_type` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`criteria_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_criteria` */

insert  into `tbl_criteria`(`criteria_id`,`criteria_name`,`criteria_level_range`,`criteria_type`) values (1,'Technical Skills','1,2,3','option'),(2,'Flexiblity','1,2,3','option'),(3,'Ug marks','Percentage','text'),(4,'Pg marks','Percentage','text'),(5,'Aptitude','1,2,3','option'),(6,'Communication skills','1,2,3','option'),(7,'SSC marks','Percentage','text'),(8,'HSC','Percentage','text');

/*Table structure for table `tbl_stud_criteria` */

DROP TABLE IF EXISTS `tbl_stud_criteria`;

CREATE TABLE `tbl_stud_criteria` (
  `stud_cri_id` int(10) NOT NULL AUTO_INCREMENT,
  `stud_id` varchar(10) NOT NULL,
  `criteria_id` varchar(25) NOT NULL,
  `criteria_level` varchar(40) NOT NULL,
  PRIMARY KEY (`stud_cri_id`)
) ENGINE=InnoDB AUTO_INCREMENT=209 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_stud_criteria` */

insert  into `tbl_stud_criteria`(`stud_cri_id`,`stud_id`,`criteria_id`,`criteria_level`) values (1,'1','3','40'),(2,'1','4','50'),(3,'1','5','1'),(4,'1','6','1'),(5,'1','7','100'),(6,'1','8','200'),(7,'1','2','1'),(8,'1','1','1'),(9,'2','3','89'),(10,'2','4','89'),(11,'2','5','1'),(12,'2','6','2'),(13,'2','7','87'),(14,'2','8','82'),(17,'3','1','2'),(18,'3','2','3'),(19,'3','3','56'),(20,'3','4','34'),(21,'3','5','2'),(22,'3','6','2'),(23,'3','7','56'),(24,'3','8','63'),(25,'4','1','1'),(26,'4','2','3'),(27,'4','3','50'),(28,'4','4','60'),(29,'4','5','2'),(30,'4','6','2'),(31,'4','7','30'),(32,'4','8','40'),(33,'5','1','3'),(34,'5','2','3'),(35,'5','3','59'),(36,'5','4','84'),(37,'5','5','2'),(38,'5','6','2'),(39,'5','7','75'),(40,'5','8','79'),(41,'6','1','1'),(42,'6','2','2'),(43,'6','3','96'),(44,'6','4','65'),(45,'6','5','2'),(46,'6','6','2'),(47,'6','7','86'),(48,'6','8','84'),(49,'7','1','1'),(50,'7','2','3'),(51,'7','3','34'),(52,'7','4','86'),(53,'7','5','3'),(54,'7','6','3'),(55,'7','7','52'),(56,'7','8','32'),(57,'8','1','3'),(58,'8','2','2'),(59,'8','3','75'),(60,'8','4','74'),(61,'8','5','2'),(62,'8','6','2'),(63,'8','7','96'),(64,'8','8','95'),(65,'9','1','3'),(66,'9','2','2'),(67,'9','3','63'),(68,'9','4','69'),(69,'9','5','2'),(70,'9','6','3'),(71,'9','7','95'),(72,'9','8','92'),(73,'10','1','2'),(74,'10','2','1'),(75,'10','3','51'),(76,'10','4','52'),(77,'10','5','2'),(78,'10','6','3'),(79,'10','7','95'),(80,'10','8','46'),(81,'11','1','3'),(82,'11','2','3'),(83,'11','3','62'),(84,'11','4','75'),(85,'11','5','2'),(86,'11','6','3'),(87,'11','7','95'),(88,'11','8','45'),(89,'12','1','3'),(90,'12','2','2'),(91,'12','3','95'),(92,'12','4','75'),(93,'12','5','1'),(94,'12','6','1'),(95,'12','7','95'),(96,'12','8','74'),(97,'13','1','1'),(98,'13','2','1'),(99,'13','3','95'),(100,'13','4','92'),(101,'13','5','1'),(102,'13','6','1'),(103,'13','7','45'),(104,'13','8','75'),(105,'14','1','3'),(106,'14','2','2'),(107,'14','3','56'),(108,'14','4','84'),(109,'14','5','1'),(110,'14','6','3'),(111,'14','7','84'),(112,'14','8','73'),(113,'15','1','1'),(114,'15','2','2'),(115,'15','3','95'),(116,'15','4','75'),(117,'15','5','2'),(118,'15','6','3'),(119,'15','7','96'),(120,'15','8','75'),(121,'16','1','1'),(122,'16','2','2'),(123,'16','3','96'),(124,'16','4','95'),(125,'16','5','2'),(126,'16','6','3'),(127,'16','7','96'),(128,'16','8','85'),(129,'17','1','3'),(130,'17','2','2'),(131,'17','3','95'),(132,'17','4','94'),(133,'17','5','3'),(134,'17','6','2'),(135,'17','7','78'),(136,'17','8','45'),(137,'18','1','3'),(138,'18','2','2'),(139,'18','3','65'),(140,'18','4','68'),(141,'18','5','3'),(142,'18','6','2'),(143,'18','7','64'),(144,'18','8','69'),(145,'19','1','3'),(146,'19','2','1'),(147,'19','3','95'),(148,'19','4','75'),(149,'19','5','3'),(150,'19','6','2'),(151,'19','7','84'),(152,'19','8','45'),(153,'20','1','3'),(154,'20','2','2'),(155,'20','3','95'),(156,'20','4','75'),(157,'20','5','2'),(158,'20','6','2'),(159,'20','7','56'),(160,'20','8','85'),(161,'21','1','1'),(162,'21','2','1'),(163,'21','3','95'),(164,'21','4','45'),(165,'21','5','3'),(166,'21','6','2'),(167,'21','7','85'),(168,'21','8','75'),(169,'22','1','1'),(170,'22','2','1'),(171,'22','3','99'),(172,'22','4','94'),(173,'22','5','3'),(174,'22','6','3'),(175,'22','7','75'),(176,'22','8','65'),(177,'23','1','2'),(178,'23','2','3'),(179,'23','3','56'),(180,'23','4','45'),(181,'23','5','2'),(182,'23','6','3'),(183,'23','7','95'),(184,'23','8','56'),(185,'24','1','3'),(186,'24','2','3'),(187,'24','3','75'),(188,'24','4','78'),(189,'24','5','2'),(190,'24','6','2'),(191,'24','7','79'),(192,'24','8','76'),(193,'25','1','2'),(194,'25','2','2'),(195,'25','3','84'),(196,'25','4','82'),(197,'25','5','3'),(198,'25','6','1'),(199,'25','7','83'),(200,'25','8','82'),(201,'27','1','3'),(202,'27','2','2'),(203,'27','3','85'),(204,'27','4','84'),(205,'27','5','3'),(206,'27','6','1'),(207,'27','7','87'),(208,'27','8','83');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
