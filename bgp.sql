-- phpMyAdmin SQL Dump
-- version 3.5.1
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 23-07-2018 a las 00:24:17
-- Versión del servidor: 5.5.24-log
-- Versión de PHP: 5.4.3

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `bgp`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dispositivos`
--

CREATE TABLE IF NOT EXISTS `dispositivos` (
  `idDispositivo` int(10) NOT NULL AUTO_INCREMENT COMMENT 'id dispositivo',
  `nombre` varchar(25) NOT NULL COMMENT 'nombre dispositivo',
  `empresa` int(10) NOT NULL COMMENT 'id empresa',
  `gateway` varchar(20) DEFAULT NULL,
  `estado` varchar(10) NOT NULL,
  PRIMARY KEY (`idDispositivo`),
  KEY `empresa` (`empresa`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Volcado de datos para la tabla `dispositivos`
--

INSERT INTO `dispositivos` (`idDispositivo`, `nombre`, `empresa`, `gateway`, `estado`) VALUES
(1, 'RouterLocal', 1, NULL, 'activo'),
(2, 'RouterRemoto', 2, NULL, 'activo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empresa`
--

CREATE TABLE IF NOT EXISTS `empresa` (
  `idEmpresa` int(10) NOT NULL AUTO_INCREMENT COMMENT 'id de la empresa',
  `nombre` varchar(50) NOT NULL COMMENT 'nombre de la empresa',
  `ASN` int(10) NOT NULL,
  PRIMARY KEY (`idEmpresa`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Volcado de datos para la tabla `empresa`
--

INSERT INTO `empresa` (`idEmpresa`, `nombre`, `ASN`) VALUES
(1, 'Empresa 1', 64512),
(2, 'Empresa 2', 64513);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `interfaces`
--

CREATE TABLE IF NOT EXISTS `interfaces` (
  `idDispositivo` int(10) NOT NULL,
  `nombre` varchar(10) NOT NULL,
  `ipAddress` varchar(20) NOT NULL,
  `mascara` varchar(20) NOT NULL,
  KEY `idDispositivo` (`idDispositivo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `interfaces`
--

INSERT INTO `interfaces` (`idDispositivo`, `nombre`, `ipAddress`, `mascara`) VALUES
(1, 'f0/0', '192.168.100.1', '255.255.255.0'),
(1, 'f4/0', '192.168.101.1', '255.255.255.0'),
(2, 'f0/0', '192.168.100.2', '255.255.255.0'),
(2, 'f4/0', '192.168.102.1', '255.255.255.0'),
(1, 's2/0', '10.1.1.1', '255.255.255.252'),
(2, 's2/0', '10.1.1.2', '255.255.255.252');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE IF NOT EXISTS `usuarios` (
  `idUsuario` int(10) NOT NULL AUTO_INCREMENT COMMENT 'Id de usuario',
  `tipo` varchar(20) NOT NULL,
  `user` varchar(30) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`idUsuario`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`idUsuario`, `tipo`, `user`, `password`) VALUES
(1, 'admin', 'jocelyn', 'jocelyn'),
(2, 'admin', 'viviana', 'viviana'),
(3, 'admin', 'edisson', 'edisson'),
(4, 'monitoreo', 'monitoreo', 'monitoreo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario_dispositivo`
--

CREATE TABLE IF NOT EXISTS `usuario_dispositivo` (
  `idUsuario` int(10) NOT NULL,
  `idDispositivo` int(10) NOT NULL,
  KEY `idUsuario` (`idUsuario`,`idDispositivo`),
  KEY `idDispositivo` (`idDispositivo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `usuario_dispositivo`
--

INSERT INTO `usuario_dispositivo` (`idUsuario`, `idDispositivo`) VALUES
(1, 1),
(1, 2),
(2, 1),
(2, 2),
(3, 1),
(3, 2);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `dispositivos`
--
ALTER TABLE `dispositivos`
  ADD CONSTRAINT `dispositivos_ibfk_1` FOREIGN KEY (`empresa`) REFERENCES `empresa` (`idEmpresa`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `interfaces`
--
ALTER TABLE `interfaces`
  ADD CONSTRAINT `interfaces_ibfk_1` FOREIGN KEY (`idDispositivo`) REFERENCES `dispositivos` (`idDispositivo`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `usuario_dispositivo`
--
ALTER TABLE `usuario_dispositivo`
  ADD CONSTRAINT `usuario_dispositivo_ibfk_1` FOREIGN KEY (`idUsuario`) REFERENCES `usuarios` (`idUsuario`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `usuario_dispositivo_ibfk_2` FOREIGN KEY (`idDispositivo`) REFERENCES `dispositivos` (`idDispositivo`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
