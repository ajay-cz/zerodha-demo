-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 24, 2017 at 09:10 PM
-- Server version: 5.7.14
-- PHP Version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `zstreamingquotesdb`
--

--
-- Database: `zstreamingquotesdb`
--
CREATE DATABASE IF NOT EXISTS `zerodhaquotesdb` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `zerodhaquotesdb`;
-- --------------------------------------------------------

--
-- Table structure for table `zerodhastreamquotes_modeltp`
--

DROP TABLE IF EXISTS `zerodhastreamquotes_modeltp`;
CREATE TABLE IF NOT EXISTS `zerodhastreamquotes_modeltp` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `InstrumentToken` varchar(32) NOT NULL,
  `Tradeable` tinyint(1) NOT NULL,
  `Timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `LastTradedPrice` decimal(20,4) NOT NULL,
  `Mode` varchar(6) NOT NULL,
   PRIMARY KEY (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
