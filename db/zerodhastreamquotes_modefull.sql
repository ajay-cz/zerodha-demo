-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 24, 2017 at 12:45 PM
-- Server version: 5.7.14
-- PHP Version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `zerodhaquotesdb`
--

-- --------------------------------------------------------
--
-- Database: `zstreamingquotesdb`
--
CREATE DATABASE IF NOT EXISTS `zerodhaquotesdb` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `zerodhaquotesdb`;

--
-- Table structure for table `zerodhastreamquotes_modefull`
--

DROP TABLE IF EXISTS `zerodhastreamquotes_modefull`;
CREATE TABLE IF NOT EXISTS `zerodhastreamquotes_modefull` (
  `Time` time NOT NULL,
  `InstrumentToken` varchar(32) NOT NULL,
  `LastTradedPrice` decimal(20,4) NOT NULL,
  `LastTradedQty` bigint(20) NOT NULL,
  `AvgTradedPrice` decimal(20,4) NOT NULL,
  `Volume` bigint(20) NOT NULL,
  `BuyQty` bigint(20) NOT NULL,
  `SellQty` bigint(20) NOT NULL,
  `OpenPrice` decimal(20,4) NOT NULL,
  `HighPrice` decimal(20,4) NOT NULL,
  `LowPrice` decimal(20,4) NOT NULL,
  `ClosePrice` decimal(20,4) NOT NULL,
  `MarketDepthBid1Qty` bigint(20) NOT NULL,
  `MarketDepthBid1Price` decimal(20,4) NOT NULL,
  `MarketDepthBid1Orders` int(11) NOT NULL,
  `MarketDepthBid2Qty` bigint(20) NOT NULL,
  `MarketDepthBid2Price` decimal(20,4) NOT NULL,
  `MarketDepthBid2Orders` int(11) NOT NULL,
  `MarketDepthBid3Qty` bigint(20) NOT NULL,
  `MarketDepthBid3Price` decimal(20,4) NOT NULL,
  `MarketDepthBid3Orders` int(11) NOT NULL,
  `MarketDepthBid4Qty` bigint(20) NOT NULL,
  `MarketDepthBid4Price` decimal(20,4) NOT NULL,
  `MarketDepthBid4Orders` int(11) NOT NULL,
  `MarketDepthBid5Qty` bigint(20) NOT NULL,
  `MarketDepthBid5Price` decimal(20,4) NOT NULL,
  `MarketDepthBid5Orders` int(11) NOT NULL,
  `MarketDepthOffer1Qty` bigint(20) NOT NULL,
  `MarketDepthOffer1Price` decimal(20,4) NOT NULL,
  `MarketDepthOffer1Orders` int(11) NOT NULL,
  `MarketDepthOffer2Qty` bigint(20) NOT NULL,
  `MarketDepthOffer2Price` decimal(20,4) NOT NULL,
  `MarketDepthOffer2Orders` int(11) NOT NULL,
  `MarketDepthOffer3Qty` bigint(20) NOT NULL,
  `MarketDepthOffer3Price` decimal(20,4) NOT NULL,
  `MarketDepthOffer3Orders` int(11) NOT NULL,
  `MarketDepthOffer4Qty` bigint(20) NOT NULL,
  `MarketDepthOffer4Price` decimal(20,4) NOT NULL,
  `MarketDepthOffer4Orders` int(11) NOT NULL,
  `MarketDepthOffer5Qty` bigint(20) NOT NULL,
  `MarketDepthOffer5Price` decimal(20,4) NOT NULL,
  `MarketDepthOffer5Orders` int(11) NOT NULL,
  PRIMARY KEY (`InstrumentToken`,`Time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
