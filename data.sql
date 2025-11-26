DROP SCHEMA IF EXISTS `lab3`;
CREATE SCHEMA IF NOT EXISTS `lab3` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `lab3`;

-- Таблиця 1: owners
CREATE TABLE IF NOT EXISTS `owners` (
  `owner_id` INT NOT NULL AUTO_INCREMENT,
  `full_name` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `phone` VARCHAR(20) NOT NULL,
  `date_of_birth` DATE NULL,
  PRIMARY KEY (`owner_id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  INDEX `idx_owners_phone` (`phone` ASC) VISIBLE
) ENGINE = InnoDB;


-- Таблиця 2: users
CREATE TABLE IF NOT EXISTS `users` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `full_name` VARCHAR(100) NOT NULL,
  `age` INT NULL,
  `gender` ENUM('male', 'female', 'other') NULL,
  `relation_to_owner` VARCHAR(50) NULL,
  PRIMARY KEY (`user_id`),
  INDEX `idx_users_name_age` (`full_name`, `age`)
) ENGINE = InnoDB;


-- Таблиця 3: addresses
CREATE TABLE IF NOT EXISTS `addresses` (
  `address_id` INT NOT NULL AUTO_INCREMENT,
  `city` VARCHAR(50) NOT NULL,
  `street` VARCHAR(100) NOT NULL,
  `house_number` VARCHAR(10) NOT NULL,
  `apartment` VARCHAR(10) NULL,
  `postal_code` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`address_id`),
  UNIQUE INDEX `idx_addresses_unique` (`city`, `street`, `house_number`)
) ENGINE = InnoDB;


-- Таблиця 4: contacts
CREATE TABLE IF NOT EXISTS `contacts` (
  `contact_id` INT NOT NULL AUTO_INCREMENT,
  `full_name` VARCHAR(100) NOT NULL,
  `phone_number` VARCHAR(20) NOT NULL,
  `email` VARCHAR(100) NULL,
  PRIMARY KEY (`contact_id`),
  INDEX `idx_contact_phone` (`phone_number`)
) ENGINE = InnoDB;


-- Таблиця 5: smartwatches
CREATE TABLE IF NOT EXISTS `smartwatches` (
  `watch_id` INT NOT NULL AUTO_INCREMENT,
  `serial_number` VARCHAR(50) NOT NULL,
  `model` VARCHAR(50) NOT NULL,
  `owner_id` INT NOT NULL,
  `address_id` INT NULL,
  `registered_date` DATE NOT NULL,
  PRIMARY KEY (`watch_id`),
  UNIQUE INDEX `serial_number_UNIQUE` (`serial_number` ASC) VISIBLE,
  CONSTRAINT `fk_sw_ownerid`
    FOREIGN KEY (`owner_id`)
    REFERENCES `owners` (`owner_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_sw_addressid`
    FOREIGN KEY (`address_id`)
    REFERENCES `addresses` (`address_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;


-- Таблиця 6: smartwatches_users
CREATE TABLE IF NOT EXISTS `smartwatches_users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `watch_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `start_date` DATE NOT NULL,
  `end_date` DATE NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `idx_swu_unique` (`watch_id`, `user_id`, `start_date`),
  CONSTRAINT `fk_swu_watchid`
    FOREIGN KEY (`watch_id`)
    REFERENCES `smartwatches` (`watch_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_swu_userid`
    FOREIGN KEY (`user_id`)
    REFERENCES `users` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;


-- Таблиця 7: telemetry
CREATE TABLE IF NOT EXISTS `telemetry` (
  `telemetry_id` INT NOT NULL AUTO_INCREMENT,
  `watch_id` INT NOT NULL,
  `timestamp` DATETIME NOT NULL,
  `heart_rate` INT NOT NULL,
  `latitude` DECIMAL(9,6) NOT NULL,
  `longitude` DECIMAL(9,6) NOT NULL,
  PRIMARY KEY (`telemetry_id`),
  UNIQUE INDEX `idx_telemetry_unique` (`watch_id`, `timestamp`),
  CONSTRAINT `fk_tel_watchid`
    FOREIGN KEY (`watch_id`)
    REFERENCES `smartwatches` (`watch_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;


-- Таблиця 8: battery_status
CREATE TABLE IF NOT EXISTS `battery_status` (
  `battery_id` INT NOT NULL AUTO_INCREMENT,
  `watch_id` INT NOT NULL,
  `timestamp` DATETIME NOT NULL,
  `battery_level` TINYINT(3) UNSIGNED NOT NULL,
  PRIMARY KEY (`battery_id`),
  UNIQUE INDEX `idx_battery_unique` (`watch_id`, `timestamp`),
  CONSTRAINT `fk_bat_watchid`
    FOREIGN KEY (`watch_id`)
    REFERENCES `smartwatches` (`watch_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;


-- Таблиця 9: alert_recipients
CREATE TABLE IF NOT EXISTS `alert_recipients` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `watch_id` INT NOT NULL,
  `contact_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `idx_recipients_unique` (`watch_id`, `contact_id`),
  CONSTRAINT `fk_ar_watchid`
    FOREIGN KEY (`watch_id`)
    REFERENCES `smartwatches` (`watch_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ar_contactid`
    FOREIGN KEY (`contact_id`)
    REFERENCES `contacts` (`contact_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;


-- Таблиця 10: alerts
CREATE TABLE IF NOT EXISTS `alerts` (
  `alert_id` INT NOT NULL AUTO_INCREMENT,
  `watch_id` INT NOT NULL,
  `recipient_id` INT NOT NULL,
  `alert_type` VARCHAR(50) NOT NULL,
  `message` TEXT(65535) NOT NULL,
  `alert_time` DATETIME NULL,
  PRIMARY KEY (`alert_id`),
  CONSTRAINT `fk_alerts_watchid`
    FOREIGN KEY (`watch_id`)
    REFERENCES `smartwatches` (`watch_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_alerts_recipientsid`
    FOREIGN KEY (`recipient_id`)
    REFERENCES `alert_recipients` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;


-- ====================================================================
-- 3. ЗАПОВНЕННЯ ДАНИМИ (10-15 INSERT у кожній таблиці)
-- ====================================================================

-- 1️⃣ OWNERS (10 записів)
INSERT INTO `owners` (`full_name`, `email`, `phone`, `date_of_birth`) VALUES
('Петро Іваненко', 'petro@mail.com', '0991111111', '1975-05-12'),
('Олена Коваль', 'olena@mail.com', '0672222222', '1980-09-01'),
('Марія Петренко', 'maria@mail.com', '0633333333', '1948-02-20'),
('Іван Сидоренко', 'ivan@mail.com', '0974444444', '1990-12-15'),
('Наталя Гнатюк', 'natalia@mail.com', '0685555555', '1985-07-30'),
('Дмитро Кравченко', 'dmytro@mail.com', '0501234567', '1995-03-25'),
('Анна Мельник', 'anna@mail.com', '0671001000', '1992-04-18'),
('Олександр Попов', 'olexandr@mail.com', '0502002000', '1970-11-05'),
('Вікторія Лисюк', 'vika@mail.com', '0633003000', '1988-01-22'),
('Максим Колос', 'maksym@mail.com', '0964004000', '1965-08-10');

-- 2️⃣ USERS (15 записів)
INSERT INTO `users` (`full_name`, `age`, `gender`, `relation_to_owner`) VALUES
('Марія Петренко', 68, 'female', 'бабуся'),
('Іван Петренко', 20, 'male', 'внук'),
('Петро Іваненко', 50, 'male', 'власник'),
('Олена Коваль', 43, 'female', 'власник'),
('Наталя Гнатюк', 38, 'female', 'сестра власника'),
('Анна Смірнова', 25, 'female', 'подруга'),
('Олег Шевченко', 30, 'male', 'син'),
('Вікторія Бойко', 55, 'female', 'мати'),
('Сергій Козак', 40, 'male', 'колега'),
('Христина Лисенко', 18, 'female', 'донька'),
('Павло Гриценко', 12, 'male', 'син'),
('Юлія Савченко', 45, 'female', 'тітка'),
('Андрій Мороз', 60, 'male', 'дядько'),
('Оксана Білик', 28, 'female', 'подруга'),
('Тарас Ковальчук', 75, 'male', 'дід');

-- 3️⃣ ADDRESSES (10 записів)
INSERT INTO `addresses` (`city`, `street`, `house_number`, `apartment`, `postal_code`) VALUES
('Львів', 'Городоцька', '10', '5', '79000'),
('Київ', 'Хрещатик', '15', '12', '01001'),
('Харків', 'Сумська', '7', NULL, '61000'),
('Одеса', 'Дерибасівська', '22', '3', '65000'),
('Дніпро', 'Центральна', '1', '8', '49000'),
('Львів', 'Наукова', '100', NULL, '79010'),
('Київ', 'Лісова', '5', '2', '02000'),
('Полтава', 'Соборна', '33', '1', '36000'),
('Черкаси', 'Шевченка', '50', NULL, '18000'),
('Суми', 'Петропавлівська', '8', '4', '40000');

-- 4️⃣ CONTACTS (10 записів)
INSERT INTO `contacts` (`full_name`, `phone_number`, `email`) VALUES
('Олексій Коваль', '0998881111', 'alex@mail.com'),
('Ірина Петренко', '0677772222', 'iryna@mail.com'),
('Сергій Іваненко', '0636663333', 'serhiy@mail.com'),
('Наталя Гнатюк', '0685554444', 'natalia@mail.com'),
('Марія Сидоренко', '0974443333', 'maria_s@mail.com'),
('Василь Сорока', '0509990000', 'vasyl@mail.com'),
('Ольга Левчук', '0671112233', 'olga@mail.com'),
('Микола Довженко', '0662224455', 'mykola@mail.com'),
('Тетяна Руденко', '0935557788', 'tatyana@mail.com'),
('Євгеній Вовк', '0981113399', 'yevhen@mail.com');

-- 5️⃣ SMARTWATCHES (12 записів)
INSERT INTO `smartwatches` (`serial_number`, `model`, `owner_id`, `address_id`, `registered_date`) VALUES
('SW1001', 'FitX', 1, 1, '2025-01-10'), -- Власник 1, Адреса 1
('SW1002', 'FitX', 2, 2, '2025-02-05'), -- Власник 2, Адреса 2
('SW1003', 'Health', 3, 3, '2025-03-01'), -- Власник 3, Адреса 3
('SW1004', 'ProWatch', 4, 4, '2025-04-10'), -- Власник 4, Адреса 4
('SW1005', 'FitX', 5, 5, '2025-05-20'), -- Власник 5, Адреса 5
('SW1006', 'Health', 1, 6, '2025-06-01'), -- Власник 1, Адреса 6
('SW1007', 'ProWatch', 2, 7, '2025-06-15'), -- Власник 2, Адреса 7
('SW1008', 'FitX', 6, 1, '2025-07-01'), -- Власник 6, Адреса 1 (спільна)
('SW1009', 'Health', 6, 2, '2025-07-10'), -- Власник 6, Адреса 2 (спільна)
('SW1010', 'ProWatch', 3, 3, '2025-07-20'), -- Власник 3, Адреса 3 (спільна)
('SW1011', 'FitX', 7, 8, '2025-08-01'), -- Власник 7, Адреса 8
('SW1012', 'Health', 8, 9, '2025-08-15'); -- Власник 8, Адреса 9

-- 6️⃣ SMARTWATCHES_USERS (12 записів)
INSERT INTO `smartwatches_users` (`watch_id`, `user_id`, `start_date`, `end_date`) VALUES
(1, 1, '2025-01-10', '2025-03-01'),
(1, 2, '2025-03-02', NULL),
(2, 4, '2025-02-05', NULL),
(3, 3, '2025-03-01', NULL),
(4, 5, '2025-04-10', NULL),
(5, 5, '2025-05-20', NULL),
(6, 6, '2025-06-01', NULL),
(7, 7, '2025-06-15', NULL),
(8, 8, '2025-07-01', NULL),
(9, 9, '2025-07-10', '2025-09-01'),
(9, 10, '2025-09-02', NULL),
(10, 3, '2025-07-20', NULL);

-- 7️⃣ TELEMETRY (15 записів)
INSERT INTO `telemetry` (`watch_id`, `timestamp`, `heart_rate`, `latitude`, `longitude`) VALUES
(1, '2025-10-29 09:00:00', 72, 49.8419, 24.0315),
(1, '2025-10-30 10:00:00', 75, 49.8418, 24.0314),
(2, '2025-10-30 10:05:00', 105, 50.4501, 30.5234),
(2, '2025-10-30 10:10:00', 70, 50.4502, 30.5235),
(3, '2025-10-30 10:15:00', 80, 49.9935, 36.2304),
(4, '2025-10-30 10:20:00', 65, 46.4825, 30.7233),
(5, '2025-10-30 10:25:00', 110, 48.4647, 35.0462),
(6, '2025-10-30 10:30:00', 68, 50.0000, 30.0000),
(7, '2025-10-30 10:35:00', 74, 51.0000, 31.0000),
(8, '2025-10-30 10:40:00', 95, 52.0000, 32.0000),
(9, '2025-10-30 10:45:00', 120, 53.0000, 33.0000),
(10, '2025-10-30 10:50:00', 78, 54.0000, 34.0000),
(11, '2025-10-30 10:55:00', 85, 49.0000, 24.0000),
(12, '2025-10-30 11:00:00', 60, 50.0000, 30.0000),
(9, '2025-10-30 11:05:00', 121, 53.0001, 33.0001);

-- 8️⃣ BATTERY_STATUS (15 записів)
INSERT INTO `battery_status` (`watch_id`, `timestamp`, `battery_level`) VALUES
(1, '2025-10-29 09:00:00', 95),
(1, '2025-10-30 10:00:00', 88),
(2, '2025-10-30 10:05:00', 15),
(2, '2025-10-30 10:10:00', 14),
(3, '2025-10-30 10:15:00', 75),
(4, '2025-10-30 10:20:00', 65),
(5, '2025-10-30 10:25:00', 10),
(6, '2025-10-30 10:30:00', 50),
(7, '2025-10-30 10:35:00', 45),
(8, '2025-10-30 10:40:00', 40),
(9, '2025-10-30 10:45:00', 35),
(10, '2025-10-30 10:50:00', 30),
(11, '2025-10-30 10:55:00', 99),
(12, '2025-10-30 11:00:00', 55),
(9, '2025-10-30 11:05:00', 34);

-- 9️⃣ ALERT_RECIPIENTS (10 записів)
INSERT INTO `alert_recipients` (`watch_id`, `contact_id`) VALUES
(1, 1), (1, 2),
(2, 2), (2, 3),
(3, 3), (3, 4),
(4, 4),
(5, 5), (5, 6),
(6, 7);

-- 🔟 ALERTS (10 записів)
INSERT INTO `alerts` (`watch_id`, `recipient_id`, `alert_type`, `message`, `alert_time`) VALUES
(1, 1, 'LowHeartRate', 'Пульс нижче 60', '2025-10-29 09:10:00'),
(2, 3, 'HighHeartRate', 'Пульс 105 уд/хв', '2025-10-30 10:06:00'),
(2, 3, 'LowBattery', 'Заряд 15%', '2025-10-30 10:07:00'),
(5, 9, 'HighHeartRate', 'Пульс 110 уд/хв', '2025-10-30 10:26:00'),
(9, 10, 'CriticalHR', 'Пульс 120 уд/хв (Критично)', '2025-10-30 10:46:00'),
(9, 10, 'CriticalHR', 'Пульс 121 уд/хв (Критично)', '2025-10-30 11:06:00'),
(10, 5, 'LocationAlert', 'Годинник 10 покинув домашню зону', '2025-10-30 11:10:00'),
(1, 2, 'LowBattery', 'Заряд 88%', '2025-10-30 11:15:00'),
(11, 4, 'ActivityAlert', 'Виявлено незвичну активність', '2025-10-30 11:20:00'),
(12, 6, 'LocationAlert', 'Годинник 12 прибув до нової зони', '2025-10-30 11:25:00');