CREATE TABLE `entity` (
  `id` integer,
  `name` char,
  `address` varchar(255),
  `pin` integer,
  `registration_id` char,
  `gst` char,
  `type` integer
);

CREATE TABLE `entity_type` (
  `id` integer PRIMARY KEY,
  `name` varchar(255) COMMENT 'Clinic/PolyClinic/Hopital'
);

CREATE TABLE `user_entity_mapping` (
  `id` integer PRIMARY KEY,
  `entity_id` integer,
  `user_id` integer,
  `isactive` varchar(255),
  `from_date` timestamp,
  `to_date` timestamp
);

CREATE TABLE `user` (
  `id` integer PRIMARY KEY,
  `username` varchar(255),
  `phonenumber` phonenumber,
  `email` email,
  `password` password,
  `registration_number` char,
  `image_path` image_path,
  `aadhar` char,
  `specialization` char,
  `role` char,
  `created_at` timestamp,
  `updated_at` timestamp
);

CREATE TABLE `user_role_mapping` (
  `user_id` integer,
  `id` integer PRIMARY KEY,
  `role_id` integer COMMENT 'One user can be be mapped to multiple roles'
);

CREATE TABLE `role` (
  `id` integer PRIMARY KEY,
  `name` char COMMENT 'Name of the role : Admin/Doctor/Recepient'
);

CREATE TABLE `appointment` (
  `id` integer PRIMARY KEY,
  `created` timestamp,
  `status` char,
  `patient_id` text COMMENT 'Content of the post',
  `specialization_id` integer,
  `doctor_id` integer,
  `created_by` char,
  `updated` timestamp,
  `updated_by` char,
  `next_appointment_date` timestamp
);

CREATE TABLE `consultation` (
  `id` integer PRIMARY KEY,
  `appointment_id` char,
  `created` timestamp,
  `status` char,
  `doctor_id` integer,
  `created_by` integer,
  `updated` timestamp,
  `updated_by` integer,
  `next_appointment_date` timestamp,
  `template_id` char,
  `consultation_fee` decimal,
  `fee_payment_status` char
);

CREATE TABLE `template_master` (
  `id` integer PRIMARY KEY,
  `template` char COMMENT 'Path to template directory'
);

CREATE TABLE `symptom_master` (
  `id` integer PRIMARY KEY,
  `symptom` char COMMENT 'All symptoms will be stored hereby'
);

CREATE TABLE `consultation_symptom` (
  `id` integer PRIMARY KEY,
  `consultation_id` char,
  `symptom_id` char
);

CREATE TABLE `consultation_medicine` (
  `id` integer PRIMARY KEY,
  `consultation_id` char,
  `medicine_id` char,
  `medicine_timing` char,
  `medicine_timing2` char,
  `medicine_dosage` char,
  `instruction` text
);

CREATE TABLE `medicine_master` (
  `id` integer PRIMARY KEY,
  `medicine_name` char,
  `medicine_dosage` char COMMENT 'Medicine Potency - Dosage'
);

CREATE TABLE `consultation_instruction` (
  `id` integer PRIMARY KEY,
  `consultation_id` char,
  `instruction` text
);

CREATE TABLE `specialization` (
  `id` integer PRIMARY KEY,
  `name` char
);

CREATE TABLE `specialization_workflow_mapping` (
  `id` integer PRIMARY KEY,
  `specialization_id` char,
  `workflow_id` char
);

CREATE TABLE `workflow` (
  `id` integer PRIMARY KEY,
  `page_name` char
);

CREATE TABLE `component` (
  `id` integer PRIMARY KEY,
  `component_name` char
);

CREATE TABLE `workflow_component_mapping` (
  `id` integer PRIMARY KEY,
  `workflow_id` char,
  `component_id` char
);

CREATE TABLE `activity_mapping` (
  `id` integer PRIMARY KEY,
  `component_id` integer,
  `entity_id` integer,
  `role_id` integer,
  `specialization_id` integer,
  `workflow_id` integer
);

CREATE TABLE `procedure` (
  `id` integer PRIMARY KEY,
  `name` char,
  `growth_required` boolean,
  `vital_required` boolean
);

CREATE TABLE `specialization_procedure_mapping` (
  `id` integer PRIMARY KEY,
  `specialization_id` integer,
  `procedure_id` integer
);

CREATE TABLE `user_specialization_procedure_mapping` (
  `id` integer PRIMARY KEY,
  `user_id` integer,
  `specialization_id` integer,
  `procedure_id` integer
);

ALTER TABLE `entity` COMMENT = 'Organisation Details';

ALTER TABLE `entity` ADD FOREIGN KEY (`type`) REFERENCES `entity_type` (`id`);

ALTER TABLE `user_entity_mapping` ADD FOREIGN KEY (`entity_id`) REFERENCES `entity` (`id`);

ALTER TABLE `activity_mapping` ADD FOREIGN KEY (`entity_id`) REFERENCES `entity` (`id`);

ALTER TABLE `user_entity_mapping` ADD FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

ALTER TABLE `user_specialization_procedure_mapping` ADD FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

ALTER TABLE `consultation` ADD FOREIGN KEY (`appointment_id`) REFERENCES `appointment` (`id`);

ALTER TABLE `consultation` ADD FOREIGN KEY (`template_id`) REFERENCES `template_master` (`id`);

ALTER TABLE `consultation_symptom` ADD FOREIGN KEY (`symptom_id`) REFERENCES `symptom_master` (`id`);

ALTER TABLE `consultation_medicine` ADD FOREIGN KEY (`medicine_id`) REFERENCES `medicine_master` (`id`);

ALTER TABLE `consultation_medicine` ADD FOREIGN KEY (`consultation_id`) REFERENCES `consultation` (`id`);

ALTER TABLE `consultation_symptom` ADD FOREIGN KEY (`consultation_id`) REFERENCES `consultation` (`id`);

ALTER TABLE `consultation_instruction` ADD FOREIGN KEY (`consultation_id`) REFERENCES `consultation` (`id`);

ALTER TABLE `user_specialization_procedure_mapping` ADD FOREIGN KEY (`procedure_id`) REFERENCES `procedure` (`id`);

ALTER TABLE `activity_mapping` ADD FOREIGN KEY (`specialization_id`) REFERENCES `specialization` (`id`);

ALTER TABLE `specialization_workflow_mapping` ADD FOREIGN KEY (`specialization_id`) REFERENCES `specialization` (`id`);

ALTER TABLE `specialization_procedure_mapping` ADD FOREIGN KEY (`specialization_id`) REFERENCES `specialization` (`id`);

ALTER TABLE `user_specialization_procedure_mapping` ADD FOREIGN KEY (`specialization_id`) REFERENCES `specialization` (`id`);

ALTER TABLE `appointment` ADD FOREIGN KEY (`specialization_id`) REFERENCES `specialization` (`id`);

ALTER TABLE `specialization_workflow_mapping` ADD FOREIGN KEY (`workflow_id`) REFERENCES `workflow` (`id`);

ALTER TABLE `workflow_component_mapping` ADD FOREIGN KEY (`workflow_id`) REFERENCES `workflow` (`id`);

ALTER TABLE `activity_mapping` ADD FOREIGN KEY (`workflow_id`) REFERENCES `workflow` (`id`);

ALTER TABLE `activity_mapping` ADD FOREIGN KEY (`component_id`) REFERENCES `component` (`id`);

ALTER TABLE `workflow_component_mapping` ADD FOREIGN KEY (`component_id`) REFERENCES `component` (`id`);

ALTER TABLE `activity_mapping` ADD FOREIGN KEY (`role_id`) REFERENCES `role` (`id`);

ALTER TABLE `user` ADD FOREIGN KEY (`role`) REFERENCES `user_role_mapping` (`id`);

ALTER TABLE `user_role_mapping` ADD FOREIGN KEY (`role_id`) REFERENCES `role` (`id`);

ALTER TABLE `user_role_mapping` ADD FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);
