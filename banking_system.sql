-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 08, 2017 at 01:59 PM
-- Server version: 5.7.14
-- PHP Version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `banking_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `id` int(5) NOT NULL,
  `customerId` int(5) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`id`, `customerId`) VALUES
(24005, 11254),
(24006, 12145);

-- --------------------------------------------------------

--
-- Table structure for table `bank`
--

CREATE TABLE `bank` (
  `BankID` int(9) NOT NULL,
  `Name` varchar(15) NOT NULL,
  `Location` varchar(15) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bank`
--

INSERT INTO `bank` (`BankID`, `Name`, `Location`) VALUES
(22224, 'skynet', 'kampala'),
(22225, 'skynet', 'jinja');

-- --------------------------------------------------------

--
-- Table structure for table `checking`
--

CREATE TABLE `checking` (
  `id` int(15) NOT NULL,
  `customerid` varchar(15) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `checking`
--

INSERT INTO `checking` (`id`, `customerid`) VALUES
(12512, '12111');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `id` varchar(15) NOT NULL,
  `Name` varchar(15) NOT NULL,
  `Address` varchar(15) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`id`, `Name`, `Address`) VALUES
('12354', 'kato', 'kawempe'),
('cm12445', 'emma', 'kawempe'),
('cm12552', 'ali', 'kabalagala'),
('00001', 'Wagalu Sadat', 'Wandegeya'),
('00002', 'Kasagga Joel', 'Kamwocha');

-- --------------------------------------------------------

--
-- Table structure for table `loan`
--

CREATE TABLE `loan` (
  `id` int(15) NOT NULL,
  `Type` varchar(15) NOT NULL,
  `Accountid` varchar(15) NOT NULL,
  `Customerid` varchar(15) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `loan`
--

INSERT INTO `loan` (`id`, `Type`, `Accountid`, `Customerid`) VALUES
(11100, 'housing', '24005', 'cm12115'),
(11101, 'investment', '24000', 'cm12500');

-- --------------------------------------------------------

--
-- Table structure for table `savings`
--

CREATE TABLE `savings` (
  `id` int(15) NOT NULL,
  `customerid` varchar(15) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `savings`
--

INSERT INTO `savings` (`id`, `customerid`) VALUES
(20112, 'cm12111'),
(20113, 'cm12311');

-- --------------------------------------------------------

--
-- Table structure for table `teller`
--

CREATE TABLE `teller` (
  `id` int(11) NOT NULL,
  `Name` varchar(15) NOT NULL,
  `CollectMoney` int(15) NOT NULL,
  `Openaccount` int(15) NOT NULL,
  `CoseAccount` int(15) NOT NULL,
  `LoanReques` int(15) NOT NULL,
  `ProvideInfo` varchar(15) NOT NULL,
  `IssueCard` varchar(15) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `teller`
--

INSERT INTO `teller` (`id`, `Name`, `CollectMoney`, `Openaccount`, `CoseAccount`, `LoanReques`, `ProvideInfo`, `IssueCard`) VALUES
(124565, 'OJAMBO JAMES', 100000, 2400622, 2400622, 5000, 'rent', 'id12465'),
(12455, 'Nakamanya Procy', 540000, 24006220, 455555, 102200, 'investment', 'id12465'),
(14255, 'Nvili Malia', 580000, 2400054, 4555555, 42000, 'housing', 'id1122'),
(12354, 'Bwogi Richard', 100000, 2400622, 200, 102200, '12 hours', 'Any time'),
(20113, 'Kato Arushad', 20001, 2400054, 200, 42000, '12 hours', '12 hours'),
(12345, 'Olwit Emmanuel', 100000, 24006220, 2400622, 102200, '12 hours', 'id12465');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bank`
--
ALTER TABLE `bank`
  ADD PRIMARY KEY (`BankID`);

--
-- Indexes for table `checking`
--
ALTER TABLE `checking`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `loan`
--
ALTER TABLE `loan`
  ADD PRIMARY KEY (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
