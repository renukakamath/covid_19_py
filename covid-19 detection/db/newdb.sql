/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 10.4.27-MariaDB : Database - alzimers_main
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`covid_19` /*!40100 DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci */;

USE `covid_19`;

/*Table structure for table `alzimers` */

DROP TABLE IF EXISTS `alzimers`;

CREATE TABLE `alzimers` (
  `alzimers_id` int(11) NOT NULL AUTO_INCREMENT,
  `alzimers` varchar(111) DEFAULT NULL,
  `details` varchar(10000) DEFAULT NULL,
  PRIMARY KEY (`alzimers_id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `alzimers` */

insert  into `alzimers`(`alzimers_id`,`alzimers`,`details`) values 
(10,'TOOTH DECAY','Tooth decay is also known as dental caries or dental cavities. It is the most common dental problem that dentists see in patients. Practically everyone, at some point in their life, has experienced tooth decay.'),
(14,'HHIH','SJSHI'),
(13,'bad smell','dfbijh');

/*Table structure for table `appointment` */

DROP TABLE IF EXISTS `appointment`;

CREATE TABLE `appointment` (
  `appointment_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `doctor_id` int(11) DEFAULT NULL,
  `appoin_date` varchar(100) DEFAULT NULL,
  `appoin_status` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT '500',
  PRIMARY KEY (`appointment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `appointment` */

insert  into `appointment`(`appointment_id`,`user_id`,`doctor_id`,`appoin_date`,`appoin_status`,`amount`) values 
(13,19,3,'2023-04-14T20:19','paid','500'),
(12,1,1,'2023-04-08T15:10','paid','500');

/*Table structure for table `doctor` */

DROP TABLE IF EXISTS `doctor`;

CREATE TABLE `doctor` (
  `doctor_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`doctor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `doctor` */

insert  into `doctor`(`doctor_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`) values 
(1,20,'ann','mary','kollam','9874561231','ann@gmail.com'),
(2,20,'an','ann','kollam','9874561230','ann@gmail.com'),
(3,22,'shyam','p','kkm','789456123','shyam@gmail.com');

/*Table structure for table `enquiry` */

DROP TABLE IF EXISTS `enquiry`;

CREATE TABLE `enquiry` (
  `equiry_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `enquiry` varchar(100) DEFAULT NULL,
  `enq_date` varchar(100) DEFAULT NULL,
  `enq_reply` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`equiry_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `enquiry` */

insert  into `enquiry`(`equiry_id`,`user_id`,`enquiry`,`enq_date`,`enq_reply`) values 
(1,1,'hai','2023-04-10','hhhh'),
(2,19,'When will the','2023-04-10','pending');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(111) DEFAULT NULL,
  `password` varchar(111) DEFAULT NULL,
  `usertype` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(2,'ju','ju','user'),
(3,'ARJUN001','ARJUN','user'),
(4,'BINDHU465','1234','user'),
(5,'balu123','1234','user'),
(6,'BALU154','1234','user'),
(7,'ADARSH401','1234','user'),
(8,'kiran456','1234','user'),
(9,'mahi001','1234','user'),
(10,'balu45','1234','user'),
(11,'leo45','1234','user'),
(12,'roy65','1234','user'),
(13,'ram65','1234','user'),
(14,'raj56','1234','user'),
(15,'rahul6554','1234','user'),
(16,'ggyg656','1234','user'),
(17,'sree456','1234','user'),
(18,'kar456','1234','user'),
(19,'jj55','1234','user'),
(20,'ann','ann','doctor'),
(21,'shyam','shyam','user'),
(22,'syam','syam','doctor');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `appointment_id` int(11) DEFAULT NULL,
  `booking_amount` varchar(100) DEFAULT NULL,
  `booking_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`appointment_id`,`booking_amount`,`booking_date`) values 
(1,12,'500','2023-04-10'),
(2,13,'500','2023-04-10'),
(3,13,'500','2023-04-10');

/*Table structure for table `prediction` */

DROP TABLE IF EXISTS `prediction`;

CREATE TABLE `prediction` (
  `prediction_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `datasuploaded` varchar(111) DEFAULT NULL,
  `output` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`prediction_id`)
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `prediction` */

insert  into `prediction`(`prediction_id`,`user_id`,`datasuploaded`,`output`) values 
(28,1,'static/uploads/a9b44c62-da84-4f8c-9bc9-843bb643757cCOVID19(0).jpg','Covid-19'),
(27,1,'static/uploads/27ebd0d7-b88d-4d23-9089-031846790379PNEUMONIA(2).jpg','Pneumonia'),
(26,1,'static/uploads/ffccb448-8177-49ed-8fef-16e5877d2372NORMAL(0).jpg','Normal'),
(25,1,'static/uploads/0e3717c2-f808-4281-868d-a97bb6536a84COVID19(0).jpg','Covid-19');

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `rating_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `rated` varchar(111) DEFAULT NULL,
  `feedback` varchar(111) DEFAULT NULL,
  `date` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`rating_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `rating` */

insert  into `rating`(`rating_id`,`user_id`,`rated`,`feedback`,`date`) values 
(8,16,'3','help full','2023-04-02'),
(7,1,'3','gkji','2023-03-30'),
(6,2,'2','IHJIHO','2023-04-04'),
(9,17,'2','good','2023-04-03');

/*Table structure for table `remady` */

DROP TABLE IF EXISTS `remady`;

CREATE TABLE `remady` (
  `remady_id` int(11) NOT NULL AUTO_INCREMENT,
  `appointment_id` int(11) DEFAULT NULL,
  `remady` varchar(100) DEFAULT NULL,
  `user_id` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`remady_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `remady` */

insert  into `remady`(`remady_id`,`appointment_id`,`remady`,`user_id`) values 
(3,13,'sxsacxsdcds','19');

/*Table structure for table `symptoms` */

DROP TABLE IF EXISTS `symptoms`;

CREATE TABLE `symptoms` (
  `symptom_id` int(11) NOT NULL AUTO_INCREMENT,
  `alzimers_id` int(11) DEFAULT NULL,
  `symptoms` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`symptom_id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `symptoms` */

insert  into `symptoms`(`symptom_id`,`alzimers_id`,`symptoms`) values 
(1,7,'BAD SMELL'),
(2,8,'BAD SMELL'),
(4,9,''),
(6,11,'weak teeth'),
(7,11,'BAD SMELL'),
(8,10,'bad smell'),
(9,12,'weak teeth'),
(11,13,'hbhbhdb');

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `firstname` varchar(111) DEFAULT NULL,
  `lastname` varchar(111) DEFAULT NULL,
  `place` varchar(111) DEFAULT NULL,
  `phone` varchar(111) DEFAULT NULL,
  `email` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `users` */

insert  into `users`(`user_id`,`login_id`,`firstname`,`lastname`,`place`,`phone`,`email`) values 
(1,2,'kjj','ljl','jlj','8766788766','xjsxn@xs.sx'),
(2,3,'ARJUN','SHABU','THURAVOOR','1456789125','ARJUN123@GMAIL.COM'),
(3,4,'BINDU','KALESH','PALLIPURAM','8111988757','BINDHU456@gmail.com'),
(4,5,'Balu','Krishna','Aluva','9865471236','balu154@gmail.com'),
(5,6,'BALU','AS','PALLIPURAM','9856741254','balu14@gmail.com'),
(6,7,'ADARSH','VARGESH','KOCHI','9854745474','adatfvvjhb745@gmail.com'),
(7,8,'kiran','kumar','KOCHI','8475621548','kiram145@g'),
(8,9,'mahi','roy','Aluva','9876543210','mahi145@gmail.com'),
(9,10,'balu','raman','cherthala','9876105432','balu414@gmail.com'),
(10,11,'leo','king','newyork','9865327410','leo123@gmail.com'),
(11,12,'roy6','joy','kochi','9856741230','roy@gmail.com'),
(12,13,'ram54','krishna','aluva','8574614666','ram@gmail.com'),
(13,14,'raj','krishna25','Aluva','4567891203','raj@gmail.com'),
(14,15,'rahul','krishna56','cherthala','6547891451','rahul@gmail.com'),
(15,16,'gyu','jnkk','cherthala','9756616132','jhbkjjb@gmail.com'),
(16,17,'sreelakshmi','krishna','kochi','9632145870','sree@gmail.com'),
(17,18,'karthi','rajive','KOCHI','7458968592','karthi@gmail.com'),
(18,19,'jkjo','djjfef','dclndlc','5478788761','dcd@gmail.com'),
(19,21,'shyam','prakash','eramangalam','7539652741','syam@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
