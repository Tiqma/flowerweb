DROP TABLE IF EXISTS flowers;

DROP PROCEDURE IF EXISTS add_flower;
DROP PROCEDURE IF EXISTS remove_all_flowers;
DROP PROCEDURE IF EXISTS remove_flower;


--
-- TABLES
--
CREATE TABLE flowers (
    `flowerid` VARCHAR(11) NOT NULL,
    `namn` varchar(45) DEFAULT NULL,
    `bildlank` varchar(45) DEFAULT NULL,
    `beskrivning` varchar(120) DEFAULT NULL,
    
    PRIMARY KEY (`flowerid`)
);


DELIMITER $$
CREATE PROCEDURE add_flower(
    In p_flowerid VARCHAR(11),
    In p_namn VARCHAR(45),
    In p_bildlank VARCHAR(45),
    In p_beskrivning VARCHAR(120)
)
BEGIN
    DECLARE v_exists INT DEFAULT 0;

    SELECT COUNT(*) INTO v_exists FROM flowers WHERE flowerid = p_flowerid;

    IF v_exists > 0 THEN
        SELECT 'exists' AS status;
    ELSE
        INSERT INTO flowers (flowerid, namn, bildlank, beskrivning)
        VALUES (p_flowerid, p_namn, p_bildlank, p_beskrivning);
        SELECT 'ok' AS status;
    END IF;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE remove_all_flowers()
BEGIN
    DELETE FROM flowers;
    SELECT 'all_removed' AS status;
END $$
DELIMITER ;


DELIMITER $$
CREATE PROCEDURE remove_flower(
    IN p_flowerid VARCHAR(11)
)

BEGIN
    DELETE FROM flowers
    WHERE flowerid = p_flowerid;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE show_flower(
    IN p_namn VARCHAR(45)
)

BEGIN
    SELECT * FROM flowers
    WHERE namn = p_namn;
END $$
DELIMITER ;