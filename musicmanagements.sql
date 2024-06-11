-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 11, 2024 at 08:03 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `musicmanagements`
--

-- --------------------------------------------------------

--
-- Table structure for table `lagu`
--

CREATE TABLE `lagu` (
  `id` int(11) NOT NULL,
  `judul` varchar(255) NOT NULL,
  `artis` varchar(255) NOT NULL,
  `album` varchar(255) DEFAULT NULL,
  `tahun_rilis` year(4) DEFAULT NULL,
  `genre` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `lagu`
--

INSERT INTO `lagu` (`id`, `judul`, `artis`, `album`, `tahun_rilis`, `genre`) VALUES
(1, 'Remedi', 'Tulus', 'Manusia', 2022, 'pop'),
(3, 'Manusia Kuat', 'Tulus', 'Monokrom', 2016, 'pop'),
(4, 'Sepatu', 'Tulus', 'Gajah', 2014, 'pop'),
(5, 'Saturn ', 'SZA', 'Saturn', 2024, 'pop'),
(6, 'Lose', 'Niki', 'Moonchild', 2020, 'pop'),
(7, 'deja vu', 'Olivia Rodrigo', 'SOUR', 2021, 'pop'),
(8, 'good 4 u', 'Olivia Rodrigo', 'SOUR', 2021, 'pop'),
(9, 'Enter Sandman', 'Metallica', 'Metallica', 1991, 'rock'),
(10, 'Glimpse of Us', 'Joji', 'SMITHEREENS', 2022, 'Indie'),
(11, 'Die For You', 'Joji', 'SMITHEREENS', 2022, 'Indie'),
(12, 'Someone Like You', 'Adele', '21', 2011, 'pop'),
(13, 'Evakuasi', 'Hindia', 'Menari Dengan Bayangan', 2019, 'Indie'),
(14, 'Hey Jude', 'The beatles', '1', 1968, 'Pop Rock');

-- --------------------------------------------------------

--
-- Table structure for table `playlist`
--

CREATE TABLE `playlist` (
  `id` int(11) NOT NULL,
  `nama_playlist` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `playlist`
--

INSERT INTO `playlist` (`id`, `nama_playlist`) VALUES
(1, 'Nangis di mobil'),
(2, 'Solo Ride'),
(3, 'Nyantai'),
(4, 'Jalan Pulang'),
(5, 'Siang Malam');

-- --------------------------------------------------------

--
-- Table structure for table `playlist_lagu`
--

CREATE TABLE `playlist_lagu` (
  `id` int(11) NOT NULL,
  `playlist_id` int(11) NOT NULL,
  `lagu_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `playlist_lagu`
--

INSERT INTO `playlist_lagu` (`id`, `playlist_id`, `lagu_id`) VALUES
(1, 1, 3),
(2, 1, 6),
(3, 1, 4),
(4, 2, 3),
(5, 4, 1),
(6, 2, 3),
(7, 2, 13);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `lagu`
--
ALTER TABLE `lagu`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `playlist`
--
ALTER TABLE `playlist`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `playlist_lagu`
--
ALTER TABLE `playlist_lagu`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_playlist` (`playlist_id`),
  ADD KEY `fk_lagu` (`lagu_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `lagu`
--
ALTER TABLE `lagu`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `playlist`
--
ALTER TABLE `playlist`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `playlist_lagu`
--
ALTER TABLE `playlist_lagu`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `playlist_lagu`
--
ALTER TABLE `playlist_lagu`
  ADD CONSTRAINT `fk_lagu` FOREIGN KEY (`lagu_id`) REFERENCES `lagu` (`id`),
  ADD CONSTRAINT `fk_playlist` FOREIGN KEY (`playlist_id`) REFERENCES `playlist` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
