-- # Class: AiRmfFramework Description: One edition of the AI RMF as a whole, with the Core and the lists the publication gives.
--     * Slot: id
--     * Slot: ai_rmf_version Description: The edition in NIST's two-number form, such as 1.0.
-- # Abstract Class: AiRmfRecord Description: The base of the classes that record an adopter's own facts, such as one of its AI systems or risks, as distinct from what the publication itself lists.
--     * Slot: ai_rmf_id Description: The identifier an adopter gives a record of its own.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: AiRmfTrustworthinessCharacteristic Description: A characteristic of trustworthy AI systems, each with a subsection of section 3.
--     * Slot: id
--     * Slot: description Description: What the element says or is.
--     * Slot: ai_rmf_characteristic_name Description: Which characteristic this is.
--     * Slot: ai_rmf_characteristic_section Description: The subsection of the publication that describes it, such as 3.1.
--     * Slot: ai_rmf_characteristic_is_base Description: Whether Figure 4 shows it as the necessary condition under the others.
--     * Slot: ai_rmf_characteristic_relates_to_all Description: Whether Figure 4 shows it relating to all the others.
--     * Slot: AiRmfFramework_id Description: Autocreated FK slot
-- # Class: AiRmfDimension Description: One of the five key socio-technical dimensions of an AI system in Figure 2.
--     * Slot: id
--     * Slot: description Description: What the element says or is.
--     * Slot: ai_rmf_dimension_name Description: Which dimension this is.
--     * Slot: ai_rmf_dimension_audience Description: The AI RMF audience formed by the AI actors in this dimension.
--     * Slot: AiRmfFramework_id Description: Autocreated FK slot
-- # Class: AiRmfLifecycleStage Description: A stage of the AI lifecycle as a column of Figure 3 shows it, under its dimension.
--     * Slot: id
--     * Slot: description Description: What the element says or is.
--     * Slot: ai_rmf_lifecycle_stage_name Description: Which stage this is.
--     * Slot: ai_rmf_lifecycle_stage_dimension Description: The dimension Figure 3 places the stage under.
--     * Slot: ai_rmf_lifecycle_stage_tevv Description: The testing, evaluation, verification and validation (TEVV) Figure 3 gives the stage.
--     * Slot: AiRmfFramework_id Description: Autocreated FK slot
-- # Class: AiRmfActorTask Description: A task or additional AI actor of Appendix A.
--     * Slot: id
--     * Slot: description Description: What the element says or is.
--     * Slot: ai_rmf_actor_task_name Description: Which task or additional AI actor this is.
--     * Slot: ai_rmf_actor_task_is_additional_actor Description: Whether Appendix A lists it under Additional AI Actors rather than as a task.
--     * Slot: AiRmfFramework_id Description: Autocreated FK slot
-- # Class: AiRmfManagementChallenge Description: One of the four challenges for AI risk management in section 1.2.
--     * Slot: id
--     * Slot: description Description: What the element says or is.
--     * Slot: ai_rmf_management_challenge_name Description: Which challenge this is.
--     * Slot: AiRmfFramework_id Description: Autocreated FK slot
-- # Class: AiRmfMeasurementChallenge Description: One of the challenges of measuring AI risk in section 1.2.1.
--     * Slot: id
--     * Slot: description Description: What the element says or is.
--     * Slot: ai_rmf_measurement_challenge_name Description: Which challenge this is.
--     * Slot: AiRmfManagementChallenge_id Description: Autocreated FK slot
-- # Class: AiRmfSpecificRisk Description: A risk that Appendix B says is new or increased for AI compared with traditional software.
--     * Slot: id
--     * Slot: title Description: This project's short name for the item. Appendix B gives its items no names.
--     * Slot: description Description: What the element says or is.
--     * Slot: ai_rmf_specific_risk_position Description: The item's position in Appendix B's list, which is not numbered.
--     * Slot: AiRmfFramework_id Description: Autocreated FK slot
-- # Class: AiRmfHumanAiIssue Description: An issue of human-AI interaction that Appendix C says merits further consideration and research.
--     * Slot: id
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
--     * Slot: ai_rmf_human_ai_issue_number Description: The issue's number in Appendix C.
--     * Slot: AiRmfFramework_id Description: Autocreated FK slot
-- # Class: AiRmfAttribute Description: A key attribute of the AI RMF in Appendix D, which guided its development.
--     * Slot: id
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
--     * Slot: ai_rmf_attribute_number Description: The attribute's number in Appendix D.
--     * Slot: AiRmfFramework_id Description: Autocreated FK slot
-- # Class: AiRmfSystem Description: An engineered or machine-based system that generates outputs such as predictions or decisions for given objectives, with varying autonomy.
--     * Slot: ai_rmf_id Description: The identifier an adopter gives a record of its own.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: AiRmfActor Description: An organization or individual with an active role in an AI system's lifecycle.
--     * Slot: ai_rmf_actor_audience Description: The AI RMF audience the actor belongs to.
--     * Slot: ai_rmf_id Description: The identifier an adopter gives a record of its own.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: AiRmfRisk Description: The composite measure of an event's probability and the magnitude of its consequences.
--     * Slot: ai_rmf_likelihood Description: How likely the event or impact is, on whatever scale the adopter uses.
--     * Slot: ai_rmf_magnitude Description: How large the consequences are, on whatever scale the adopter uses.
--     * Slot: ai_rmf_risk_system Description: The AI system the risk concerns.
--     * Slot: ai_rmf_id Description: The identifier an adopter gives a record of its own.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: AiRmfResidualRisk Description: The risk that remains after risk treatment.
--     * Slot: ai_rmf_likelihood Description: How likely the event or impact is, on whatever scale the adopter uses.
--     * Slot: ai_rmf_magnitude Description: How large the consequences are, on whatever scale the adopter uses.
--     * Slot: ai_rmf_risk_system Description: The AI system the risk concerns.
--     * Slot: ai_rmf_id Description: The identifier an adopter gives a record of its own.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: AiRmfImpact Description: A consequence of an AI system, which may be an opportunity, a threat or both.
--     * Slot: ai_rmf_likelihood Description: How likely the event or impact is, on whatever scale the adopter uses.
--     * Slot: ai_rmf_magnitude Description: How large the consequences are, on whatever scale the adopter uses.
--     * Slot: ai_rmf_impact_direction Description: Whether the consequence is positive, negative or both.
--     * Slot: ai_rmf_id Description: The identifier an adopter gives a record of its own.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
--     * Slot: AiRmfRisk_ai_rmf_id Description: Autocreated FK slot
--     * Slot: AiRmfResidualRisk_ai_rmf_id Description: Autocreated FK slot
-- # Class: AiRmfHarm Description: A negative impact, sorted as in Figure 1 by whether it falls on people, an organization or an ecosystem.
--     * Slot: ai_rmf_harm_category Description: The heading of Figure 1 the harm falls under.
--     * Slot: ai_rmf_harm_example Description: The example of Figure 1 the harm matches, which must sit under the harm's category.
--     * Slot: ai_rmf_likelihood Description: How likely the event or impact is, on whatever scale the adopter uses.
--     * Slot: ai_rmf_magnitude Description: How large the consequences are, on whatever scale the adopter uses.
--     * Slot: ai_rmf_impact_direction Description: Whether the consequence is positive, negative or both.
--     * Slot: ai_rmf_id Description: The identifier an adopter gives a record of its own.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: AiRmfRiskTolerance Description: An organization's or AI actor's readiness to bear risk to achieve its objectives. The AI RMF prescribes none.
--     * Slot: ai_rmf_risk_tolerance_holder Description: The organization or AI actor whose tolerance this is.
--     * Slot: ai_rmf_id Description: The identifier an adopter gives a record of its own.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: AiRmfBias Description: A bias to consider and manage, sorted into NIST's three major categories.
--     * Slot: ai_rmf_id Description: The identifier an adopter gives a record of its own.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: AiRmfFunction Description: One of the four functions that organize AI risk management at the highest level. GOVERN cuts across the other three.
--     * Slot: id
--     * Slot: ai_rmf_function_id Description: The function's name, such as GOVERN.
--     * Slot: description Description: The one-sentence overview in NIST's catalog. The publication gives each function a section of its own instead.
--     * Slot: AiRmfFramework_id Description: Autocreated FK slot
-- # Class: AiRmfCategory Description: A group of related outcomes within a function, such as GOVERN 1, which Tables 1 to 4 state.
--     * Slot: id
--     * Slot: ai_rmf_category_id Description: The category's identifier, such as GOVERN 1.
--     * Slot: description Description: The category's statement in the publication.
--     * Slot: AiRmfFunction_id Description: Autocreated FK slot
-- # Class: AiRmfSubcategory Description: A specific outcome within a category, such as GOVERN 1.1, which Tables 1 to 4 state, and its Playbook material.
--     * Slot: id
--     * Slot: ai_rmf_subcategory_id Description: The subcategory's identifier, such as GOVERN 1.1.
--     * Slot: description Description: The subcategory's statement in the publication.
--     * Slot: AiRmfCategory_id Description: Autocreated FK slot
-- # Class: AiRmfSuggestedAction Description: One step the Playbook suggests towards a subcategory's outcome.
--     * Slot: id
--     * Slot: ai_rmf_suggested_action_id Description: The suggested action's identifier, such as SA-GOVERN_1.1-1.
--     * Slot: description Description: What the element says or is.
--     * Slot: AiRmfSubcategory_id Description: Autocreated FK slot
-- # Class: AiRmfDocumentationItem Description: One thing the Playbook suggests an organization document for a subcategory.
--     * Slot: id
--     * Slot: ai_rmf_documentation_id Description: The documentation prompt's identifier, such as D-GOVERN_1.1-1.
--     * Slot: description Description: What the element says or is.
--     * Slot: AiRmfSubcategory_id Description: Autocreated FK slot
-- # Class: AiRmfResource Description: A source the Playbook points to, by the title and address NIST's catalog gives it.
--     * Slot: id
--     * Slot: title Description: The element's name.
--     * Slot: ai_rmf_resource_uuid Description: The UUID of the resource in the back matter of NIST's catalog.
--     * Slot: ai_rmf_resource_address Description: The address NIST's catalog gives the source. The catalog gives none for a few.
--     * Slot: AiRmfSubcategory_id Description: Autocreated FK slot
-- # Class: AiRmfProfile Description: An implementation of the Core's functions, categories and subcategories for a setting, application or technology, based on the adopter's requirements, risk tolerance and resources.
--     * Slot: ai_rmf_profile_setting Description: The sector, industry, technology, organization or end use the profile covers, such as hiring.
--     * Slot: ai_rmf_id Description: The identifier an adopter gives a record of its own.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: AiRmfLifecycleStage_ai_rmf_lifecycle_stage_representative_actors
--     * Slot: AiRmfLifecycleStage_id Description: Autocreated FK slot
--     * Slot: ai_rmf_lifecycle_stage_representative_actors Description: The representative AI actors Figure 3 lists for the stage.
-- # Class: AiRmfActorTask_ai_rmf_actor_task_representative_actors
--     * Slot: AiRmfActorTask_id Description: Autocreated FK slot
--     * Slot: ai_rmf_actor_task_representative_actors Description: The AI actors that Appendix A says carry out the task.
-- # Class: AiRmfSystem_ai_rmf_system_lifecycle_stages
--     * Slot: AiRmfSystem_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_system_lifecycle_stages Description: The lifecycle stages the record covers.
-- # Class: AiRmfActor_ai_rmf_actor_tasks
--     * Slot: AiRmfActor_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_actor_tasks Description: The tasks the actor carries out, or the additional AI actor it is.
-- # Class: AiRmfActor_ai_rmf_actor_lifecycle_stages
--     * Slot: AiRmfActor_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_actor_lifecycle_stages Description: The lifecycle stages the actor works in.
-- # Class: AiRmfRisk_ai_rmf_risk_characteristics
--     * Slot: AiRmfRisk_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_risk_characteristics Description: The trustworthiness characteristics the risk bears on.
-- # Class: AiRmfRisk_ai_rmf_risk_lifecycle_stages
--     * Slot: AiRmfRisk_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_risk_lifecycle_stages Description: The lifecycle stages where the risk is measured or arises.
-- # Class: AiRmfRisk_ai_rmf_risk_responses
--     * Slot: AiRmfRisk_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_risk_responses Description: The responses chosen for the risk.
-- # Class: AiRmfResidualRisk_ai_rmf_risk_characteristics
--     * Slot: AiRmfResidualRisk_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_risk_characteristics Description: The trustworthiness characteristics the risk bears on.
-- # Class: AiRmfResidualRisk_ai_rmf_risk_lifecycle_stages
--     * Slot: AiRmfResidualRisk_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_risk_lifecycle_stages Description: The lifecycle stages where the risk is measured or arises.
-- # Class: AiRmfResidualRisk_ai_rmf_risk_responses
--     * Slot: AiRmfResidualRisk_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_risk_responses Description: The responses chosen for the risk.
-- # Class: AiRmfImpact_ai_rmf_impact_affected_parties
--     * Slot: AiRmfImpact_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_impact_affected_parties Description: Who or what experiences the consequence.
-- # Class: AiRmfHarm_ai_rmf_impact_affected_parties
--     * Slot: AiRmfHarm_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_impact_affected_parties Description: Who or what experiences the consequence.
-- # Class: AiRmfRiskTolerance_ai_rmf_risk_tolerance_influences
--     * Slot: AiRmfRiskTolerance_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_risk_tolerance_influences Description: What influences it, such as a law, a regulation, a policy or a norm.
-- # Class: AiRmfBias_ai_rmf_bias_categories
--     * Slot: AiRmfBias_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_bias_categories Description: The categories it falls under.
-- # Class: AiRmfSubcategory_ai_rmf_subcategory_about
--     * Slot: AiRmfSubcategory_id Description: Autocreated FK slot
--     * Slot: ai_rmf_subcategory_about Description: The Playbook's discussion of the outcome.
-- # Class: AiRmfSubcategory_ai_rmf_subcategory_ai_actors
--     * Slot: AiRmfSubcategory_id Description: Autocreated FK slot
--     * Slot: ai_rmf_subcategory_ai_actors Description: The AI actors the Playbook tags the outcome with.
-- # Class: AiRmfSubcategory_ai_rmf_subcategory_topics
--     * Slot: AiRmfSubcategory_id Description: Autocreated FK slot
--     * Slot: ai_rmf_subcategory_topics Description: The topics the Playbook tags the outcome with. NIST keeps no closed list of them.
-- # Class: AiRmfProfile_ai_rmf_profile_kinds
--     * Slot: AiRmfProfile_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_profile_kinds Description: Which of the publication's kinds of profile this is. A current profile for one use case is both.
-- # Class: AiRmfProfile_ai_rmf_profile_subcategories
--     * Slot: AiRmfProfile_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_profile_subcategories Description: The subcategories the profile selects. An adopter may select from them rather than apply all.

CREATE TABLE "AiRmfFramework" (
	id INTEGER NOT NULL,
	ai_rmf_version TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AiRmfFramework_id" ON "AiRmfFramework" (id);

CREATE TABLE "AiRmfRecord" (
	ai_rmf_id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfRecord_ai_rmf_id" ON "AiRmfRecord" (ai_rmf_id);

CREATE TABLE "AiRmfSystem" (
	ai_rmf_id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfSystem_ai_rmf_id" ON "AiRmfSystem" (ai_rmf_id);

CREATE TABLE "AiRmfActor" (
	ai_rmf_actor_audience VARCHAR(9),
	ai_rmf_id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfActor_ai_rmf_id" ON "AiRmfActor" (ai_rmf_id);

CREATE TABLE "AiRmfHarm" (
	ai_rmf_harm_category VARCHAR(12) NOT NULL,
	ai_rmf_harm_example VARCHAR(33),
	ai_rmf_likelihood TEXT,
	ai_rmf_magnitude TEXT,
	ai_rmf_impact_direction VARCHAR(8) NOT NULL,
	ai_rmf_id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfHarm_ai_rmf_id" ON "AiRmfHarm" (ai_rmf_id);

CREATE TABLE "AiRmfBias" (
	ai_rmf_id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfBias_ai_rmf_id" ON "AiRmfBias" (ai_rmf_id);

CREATE TABLE "AiRmfProfile" (
	ai_rmf_profile_setting TEXT,
	ai_rmf_id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfProfile_ai_rmf_id" ON "AiRmfProfile" (ai_rmf_id);

CREATE TABLE "AiRmfTrustworthinessCharacteristic" (
	id INTEGER NOT NULL,
	description TEXT,
	ai_rmf_characteristic_name VARCHAR(30) NOT NULL,
	ai_rmf_characteristic_section TEXT NOT NULL,
	ai_rmf_characteristic_is_base BOOLEAN,
	ai_rmf_characteristic_relates_to_all BOOLEAN,
	"AiRmfFramework_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFramework_id") REFERENCES "AiRmfFramework" (id)
);
CREATE INDEX "ix_AiRmfTrustworthinessCharacteristic_id" ON "AiRmfTrustworthinessCharacteristic" (id);

CREATE TABLE "AiRmfDimension" (
	id INTEGER NOT NULL,
	description TEXT,
	ai_rmf_dimension_name VARCHAR(19) NOT NULL,
	ai_rmf_dimension_audience VARCHAR(9) NOT NULL,
	"AiRmfFramework_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFramework_id") REFERENCES "AiRmfFramework" (id)
);
CREATE INDEX "ix_AiRmfDimension_id" ON "AiRmfDimension" (id);

CREATE TABLE "AiRmfLifecycleStage" (
	id INTEGER NOT NULL,
	description TEXT,
	ai_rmf_lifecycle_stage_name VARCHAR(24) NOT NULL,
	ai_rmf_lifecycle_stage_dimension VARCHAR(19) NOT NULL,
	ai_rmf_lifecycle_stage_tevv TEXT,
	"AiRmfFramework_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFramework_id") REFERENCES "AiRmfFramework" (id)
);
CREATE INDEX "ix_AiRmfLifecycleStage_id" ON "AiRmfLifecycleStage" (id);

CREATE TABLE "AiRmfActorTask" (
	id INTEGER NOT NULL,
	description TEXT,
	ai_rmf_actor_task_name VARCHAR(36) NOT NULL,
	ai_rmf_actor_task_is_additional_actor BOOLEAN,
	"AiRmfFramework_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFramework_id") REFERENCES "AiRmfFramework" (id)
);
CREATE INDEX "ix_AiRmfActorTask_id" ON "AiRmfActorTask" (id);

CREATE TABLE "AiRmfManagementChallenge" (
	id INTEGER NOT NULL,
	description TEXT,
	ai_rmf_management_challenge_name VARCHAR(49) NOT NULL,
	"AiRmfFramework_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFramework_id") REFERENCES "AiRmfFramework" (id)
);
CREATE INDEX "ix_AiRmfManagementChallenge_id" ON "AiRmfManagementChallenge" (id);

CREATE TABLE "AiRmfSpecificRisk" (
	id INTEGER NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	ai_rmf_specific_risk_position INTEGER NOT NULL,
	"AiRmfFramework_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFramework_id") REFERENCES "AiRmfFramework" (id)
);
CREATE INDEX "ix_AiRmfSpecificRisk_id" ON "AiRmfSpecificRisk" (id);

CREATE TABLE "AiRmfHumanAiIssue" (
	id INTEGER NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	ai_rmf_human_ai_issue_number INTEGER NOT NULL,
	"AiRmfFramework_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFramework_id") REFERENCES "AiRmfFramework" (id)
);
CREATE INDEX "ix_AiRmfHumanAiIssue_id" ON "AiRmfHumanAiIssue" (id);

CREATE TABLE "AiRmfAttribute" (
	id INTEGER NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	ai_rmf_attribute_number INTEGER NOT NULL,
	"AiRmfFramework_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFramework_id") REFERENCES "AiRmfFramework" (id)
);
CREATE INDEX "ix_AiRmfAttribute_id" ON "AiRmfAttribute" (id);

CREATE TABLE "AiRmfRisk" (
	ai_rmf_likelihood TEXT,
	ai_rmf_magnitude TEXT,
	ai_rmf_risk_system TEXT,
	ai_rmf_id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (ai_rmf_id),
	FOREIGN KEY(ai_rmf_risk_system) REFERENCES "AiRmfSystem" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfRisk_ai_rmf_id" ON "AiRmfRisk" (ai_rmf_id);

CREATE TABLE "AiRmfResidualRisk" (
	ai_rmf_likelihood TEXT,
	ai_rmf_magnitude TEXT,
	ai_rmf_risk_system TEXT,
	ai_rmf_id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (ai_rmf_id),
	FOREIGN KEY(ai_rmf_risk_system) REFERENCES "AiRmfSystem" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfResidualRisk_ai_rmf_id" ON "AiRmfResidualRisk" (ai_rmf_id);

CREATE TABLE "AiRmfRiskTolerance" (
	ai_rmf_risk_tolerance_holder TEXT,
	ai_rmf_id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (ai_rmf_id),
	FOREIGN KEY(ai_rmf_risk_tolerance_holder) REFERENCES "AiRmfActor" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfRiskTolerance_ai_rmf_id" ON "AiRmfRiskTolerance" (ai_rmf_id);

CREATE TABLE "AiRmfFunction" (
	id INTEGER NOT NULL,
	ai_rmf_function_id TEXT NOT NULL,
	description TEXT,
	"AiRmfFramework_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFramework_id") REFERENCES "AiRmfFramework" (id)
);
CREATE INDEX "ix_AiRmfFunction_id" ON "AiRmfFunction" (id);

CREATE TABLE "AiRmfSystem_ai_rmf_system_lifecycle_stages" (
	"AiRmfSystem_ai_rmf_id" TEXT,
	ai_rmf_system_lifecycle_stages VARCHAR(24),
	PRIMARY KEY ("AiRmfSystem_ai_rmf_id", ai_rmf_system_lifecycle_stages),
	FOREIGN KEY("AiRmfSystem_ai_rmf_id") REFERENCES "AiRmfSystem" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfSystem_ai_rmf_system_lifecycle_stages_ai_rmf_system_lifecycle_stages" ON "AiRmfSystem_ai_rmf_system_lifecycle_stages" (ai_rmf_system_lifecycle_stages);
CREATE INDEX "ix_AiRmfSystem_ai_rmf_system_lifecycle_stages_AiRmfSystem_ai_rmf_id" ON "AiRmfSystem_ai_rmf_system_lifecycle_stages" ("AiRmfSystem_ai_rmf_id");

CREATE TABLE "AiRmfActor_ai_rmf_actor_tasks" (
	"AiRmfActor_ai_rmf_id" TEXT,
	ai_rmf_actor_tasks VARCHAR(36),
	PRIMARY KEY ("AiRmfActor_ai_rmf_id", ai_rmf_actor_tasks),
	FOREIGN KEY("AiRmfActor_ai_rmf_id") REFERENCES "AiRmfActor" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfActor_ai_rmf_actor_tasks_ai_rmf_actor_tasks" ON "AiRmfActor_ai_rmf_actor_tasks" (ai_rmf_actor_tasks);
CREATE INDEX "ix_AiRmfActor_ai_rmf_actor_tasks_AiRmfActor_ai_rmf_id" ON "AiRmfActor_ai_rmf_actor_tasks" ("AiRmfActor_ai_rmf_id");

CREATE TABLE "AiRmfActor_ai_rmf_actor_lifecycle_stages" (
	"AiRmfActor_ai_rmf_id" TEXT,
	ai_rmf_actor_lifecycle_stages VARCHAR(24),
	PRIMARY KEY ("AiRmfActor_ai_rmf_id", ai_rmf_actor_lifecycle_stages),
	FOREIGN KEY("AiRmfActor_ai_rmf_id") REFERENCES "AiRmfActor" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfActor_ai_rmf_actor_lifecycle_stages_AiRmfActor_ai_rmf_id" ON "AiRmfActor_ai_rmf_actor_lifecycle_stages" ("AiRmfActor_ai_rmf_id");
CREATE INDEX "ix_AiRmfActor_ai_rmf_actor_lifecycle_stages_ai_rmf_actor_lifecycle_stages" ON "AiRmfActor_ai_rmf_actor_lifecycle_stages" (ai_rmf_actor_lifecycle_stages);

CREATE TABLE "AiRmfHarm_ai_rmf_impact_affected_parties" (
	"AiRmfHarm_ai_rmf_id" TEXT,
	ai_rmf_impact_affected_parties VARCHAR(13),
	PRIMARY KEY ("AiRmfHarm_ai_rmf_id", ai_rmf_impact_affected_parties),
	FOREIGN KEY("AiRmfHarm_ai_rmf_id") REFERENCES "AiRmfHarm" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfHarm_ai_rmf_impact_affected_parties_ai_rmf_impact_affected_parties" ON "AiRmfHarm_ai_rmf_impact_affected_parties" (ai_rmf_impact_affected_parties);
CREATE INDEX "ix_AiRmfHarm_ai_rmf_impact_affected_parties_AiRmfHarm_ai_rmf_id" ON "AiRmfHarm_ai_rmf_impact_affected_parties" ("AiRmfHarm_ai_rmf_id");

CREATE TABLE "AiRmfBias_ai_rmf_bias_categories" (
	"AiRmfBias_ai_rmf_id" TEXT,
	ai_rmf_bias_categories VARCHAR(29) NOT NULL,
	PRIMARY KEY ("AiRmfBias_ai_rmf_id", ai_rmf_bias_categories),
	FOREIGN KEY("AiRmfBias_ai_rmf_id") REFERENCES "AiRmfBias" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfBias_ai_rmf_bias_categories_AiRmfBias_ai_rmf_id" ON "AiRmfBias_ai_rmf_bias_categories" ("AiRmfBias_ai_rmf_id");
CREATE INDEX "ix_AiRmfBias_ai_rmf_bias_categories_ai_rmf_bias_categories" ON "AiRmfBias_ai_rmf_bias_categories" (ai_rmf_bias_categories);

CREATE TABLE "AiRmfProfile_ai_rmf_profile_kinds" (
	"AiRmfProfile_ai_rmf_id" TEXT,
	ai_rmf_profile_kinds VARCHAR(14) NOT NULL,
	PRIMARY KEY ("AiRmfProfile_ai_rmf_id", ai_rmf_profile_kinds),
	FOREIGN KEY("AiRmfProfile_ai_rmf_id") REFERENCES "AiRmfProfile" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfProfile_ai_rmf_profile_kinds_ai_rmf_profile_kinds" ON "AiRmfProfile_ai_rmf_profile_kinds" (ai_rmf_profile_kinds);
CREATE INDEX "ix_AiRmfProfile_ai_rmf_profile_kinds_AiRmfProfile_ai_rmf_id" ON "AiRmfProfile_ai_rmf_profile_kinds" ("AiRmfProfile_ai_rmf_id");

CREATE TABLE "AiRmfProfile_ai_rmf_profile_subcategories" (
	"AiRmfProfile_ai_rmf_id" TEXT,
	ai_rmf_profile_subcategories TEXT,
	PRIMARY KEY ("AiRmfProfile_ai_rmf_id", ai_rmf_profile_subcategories),
	FOREIGN KEY("AiRmfProfile_ai_rmf_id") REFERENCES "AiRmfProfile" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfProfile_ai_rmf_profile_subcategories_ai_rmf_profile_subcategories" ON "AiRmfProfile_ai_rmf_profile_subcategories" (ai_rmf_profile_subcategories);
CREATE INDEX "ix_AiRmfProfile_ai_rmf_profile_subcategories_AiRmfProfile_ai_rmf_id" ON "AiRmfProfile_ai_rmf_profile_subcategories" ("AiRmfProfile_ai_rmf_id");

CREATE TABLE "AiRmfMeasurementChallenge" (
	id INTEGER NOT NULL,
	description TEXT,
	ai_rmf_measurement_challenge_name VARCHAR(38) NOT NULL,
	"AiRmfManagementChallenge_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfManagementChallenge_id") REFERENCES "AiRmfManagementChallenge" (id)
);
CREATE INDEX "ix_AiRmfMeasurementChallenge_id" ON "AiRmfMeasurementChallenge" (id);

CREATE TABLE "AiRmfImpact" (
	ai_rmf_likelihood TEXT,
	ai_rmf_magnitude TEXT,
	ai_rmf_impact_direction VARCHAR(8) NOT NULL,
	ai_rmf_id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"AiRmfRisk_ai_rmf_id" TEXT,
	"AiRmfResidualRisk_ai_rmf_id" TEXT,
	PRIMARY KEY (ai_rmf_id),
	FOREIGN KEY("AiRmfRisk_ai_rmf_id") REFERENCES "AiRmfRisk" (ai_rmf_id),
	FOREIGN KEY("AiRmfResidualRisk_ai_rmf_id") REFERENCES "AiRmfResidualRisk" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfImpact_ai_rmf_id" ON "AiRmfImpact" (ai_rmf_id);

CREATE TABLE "AiRmfCategory" (
	id INTEGER NOT NULL,
	ai_rmf_category_id TEXT NOT NULL,
	description TEXT NOT NULL,
	"AiRmfFunction_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFunction_id") REFERENCES "AiRmfFunction" (id)
);
CREATE INDEX "ix_AiRmfCategory_id" ON "AiRmfCategory" (id);

CREATE TABLE "AiRmfLifecycleStage_ai_rmf_lifecycle_stage_representative_actors" (
	"AiRmfLifecycleStage_id" INTEGER,
	ai_rmf_lifecycle_stage_representative_actors TEXT,
	PRIMARY KEY ("AiRmfLifecycleStage_id", ai_rmf_lifecycle_stage_representative_actors),
	FOREIGN KEY("AiRmfLifecycleStage_id") REFERENCES "AiRmfLifecycleStage" (id)
);
CREATE INDEX "ix_AiRmfLifecycleStage_ai_rmf_lifecycle_stage_representative_actors_ai_rmf_lifecycle_stage_representative_actors" ON "AiRmfLifecycleStage_ai_rmf_lifecycle_stage_representative_actors" (ai_rmf_lifecycle_stage_representative_actors);
CREATE INDEX "ix_AiRmfLifecycleStage_ai_rmf_lifecycle_stage_representative_actors_AiRmfLifecycleStage_id" ON "AiRmfLifecycleStage_ai_rmf_lifecycle_stage_representative_actors" ("AiRmfLifecycleStage_id");

CREATE TABLE "AiRmfActorTask_ai_rmf_actor_task_representative_actors" (
	"AiRmfActorTask_id" INTEGER,
	ai_rmf_actor_task_representative_actors TEXT,
	PRIMARY KEY ("AiRmfActorTask_id", ai_rmf_actor_task_representative_actors),
	FOREIGN KEY("AiRmfActorTask_id") REFERENCES "AiRmfActorTask" (id)
);
CREATE INDEX "ix_AiRmfActorTask_ai_rmf_actor_task_representative_actors_ai_rmf_actor_task_representative_actors" ON "AiRmfActorTask_ai_rmf_actor_task_representative_actors" (ai_rmf_actor_task_representative_actors);
CREATE INDEX "ix_AiRmfActorTask_ai_rmf_actor_task_representative_actors_AiRmfActorTask_id" ON "AiRmfActorTask_ai_rmf_actor_task_representative_actors" ("AiRmfActorTask_id");

CREATE TABLE "AiRmfRisk_ai_rmf_risk_characteristics" (
	"AiRmfRisk_ai_rmf_id" TEXT,
	ai_rmf_risk_characteristics VARCHAR(30),
	PRIMARY KEY ("AiRmfRisk_ai_rmf_id", ai_rmf_risk_characteristics),
	FOREIGN KEY("AiRmfRisk_ai_rmf_id") REFERENCES "AiRmfRisk" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfRisk_ai_rmf_risk_characteristics_AiRmfRisk_ai_rmf_id" ON "AiRmfRisk_ai_rmf_risk_characteristics" ("AiRmfRisk_ai_rmf_id");
CREATE INDEX "ix_AiRmfRisk_ai_rmf_risk_characteristics_ai_rmf_risk_characteristics" ON "AiRmfRisk_ai_rmf_risk_characteristics" (ai_rmf_risk_characteristics);

CREATE TABLE "AiRmfRisk_ai_rmf_risk_lifecycle_stages" (
	"AiRmfRisk_ai_rmf_id" TEXT,
	ai_rmf_risk_lifecycle_stages VARCHAR(24),
	PRIMARY KEY ("AiRmfRisk_ai_rmf_id", ai_rmf_risk_lifecycle_stages),
	FOREIGN KEY("AiRmfRisk_ai_rmf_id") REFERENCES "AiRmfRisk" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfRisk_ai_rmf_risk_lifecycle_stages_AiRmfRisk_ai_rmf_id" ON "AiRmfRisk_ai_rmf_risk_lifecycle_stages" ("AiRmfRisk_ai_rmf_id");
CREATE INDEX "ix_AiRmfRisk_ai_rmf_risk_lifecycle_stages_ai_rmf_risk_lifecycle_stages" ON "AiRmfRisk_ai_rmf_risk_lifecycle_stages" (ai_rmf_risk_lifecycle_stages);

CREATE TABLE "AiRmfRisk_ai_rmf_risk_responses" (
	"AiRmfRisk_ai_rmf_id" TEXT,
	ai_rmf_risk_responses VARCHAR(12),
	PRIMARY KEY ("AiRmfRisk_ai_rmf_id", ai_rmf_risk_responses),
	FOREIGN KEY("AiRmfRisk_ai_rmf_id") REFERENCES "AiRmfRisk" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfRisk_ai_rmf_risk_responses_ai_rmf_risk_responses" ON "AiRmfRisk_ai_rmf_risk_responses" (ai_rmf_risk_responses);
CREATE INDEX "ix_AiRmfRisk_ai_rmf_risk_responses_AiRmfRisk_ai_rmf_id" ON "AiRmfRisk_ai_rmf_risk_responses" ("AiRmfRisk_ai_rmf_id");

CREATE TABLE "AiRmfResidualRisk_ai_rmf_risk_characteristics" (
	"AiRmfResidualRisk_ai_rmf_id" TEXT,
	ai_rmf_risk_characteristics VARCHAR(30),
	PRIMARY KEY ("AiRmfResidualRisk_ai_rmf_id", ai_rmf_risk_characteristics),
	FOREIGN KEY("AiRmfResidualRisk_ai_rmf_id") REFERENCES "AiRmfResidualRisk" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfResidualRisk_ai_rmf_risk_characteristics_ai_rmf_risk_characteristics" ON "AiRmfResidualRisk_ai_rmf_risk_characteristics" (ai_rmf_risk_characteristics);
CREATE INDEX "ix_AiRmfResidualRisk_ai_rmf_risk_characteristics_AiRmfResidualRisk_ai_rmf_id" ON "AiRmfResidualRisk_ai_rmf_risk_characteristics" ("AiRmfResidualRisk_ai_rmf_id");

CREATE TABLE "AiRmfResidualRisk_ai_rmf_risk_lifecycle_stages" (
	"AiRmfResidualRisk_ai_rmf_id" TEXT,
	ai_rmf_risk_lifecycle_stages VARCHAR(24),
	PRIMARY KEY ("AiRmfResidualRisk_ai_rmf_id", ai_rmf_risk_lifecycle_stages),
	FOREIGN KEY("AiRmfResidualRisk_ai_rmf_id") REFERENCES "AiRmfResidualRisk" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfResidualRisk_ai_rmf_risk_lifecycle_stages_AiRmfResidualRisk_ai_rmf_id" ON "AiRmfResidualRisk_ai_rmf_risk_lifecycle_stages" ("AiRmfResidualRisk_ai_rmf_id");
CREATE INDEX "ix_AiRmfResidualRisk_ai_rmf_risk_lifecycle_stages_ai_rmf_risk_lifecycle_stages" ON "AiRmfResidualRisk_ai_rmf_risk_lifecycle_stages" (ai_rmf_risk_lifecycle_stages);

CREATE TABLE "AiRmfResidualRisk_ai_rmf_risk_responses" (
	"AiRmfResidualRisk_ai_rmf_id" TEXT,
	ai_rmf_risk_responses VARCHAR(12),
	PRIMARY KEY ("AiRmfResidualRisk_ai_rmf_id", ai_rmf_risk_responses),
	FOREIGN KEY("AiRmfResidualRisk_ai_rmf_id") REFERENCES "AiRmfResidualRisk" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfResidualRisk_ai_rmf_risk_responses_ai_rmf_risk_responses" ON "AiRmfResidualRisk_ai_rmf_risk_responses" (ai_rmf_risk_responses);
CREATE INDEX "ix_AiRmfResidualRisk_ai_rmf_risk_responses_AiRmfResidualRisk_ai_rmf_id" ON "AiRmfResidualRisk_ai_rmf_risk_responses" ("AiRmfResidualRisk_ai_rmf_id");

CREATE TABLE "AiRmfRiskTolerance_ai_rmf_risk_tolerance_influences" (
	"AiRmfRiskTolerance_ai_rmf_id" TEXT,
	ai_rmf_risk_tolerance_influences TEXT,
	PRIMARY KEY ("AiRmfRiskTolerance_ai_rmf_id", ai_rmf_risk_tolerance_influences),
	FOREIGN KEY("AiRmfRiskTolerance_ai_rmf_id") REFERENCES "AiRmfRiskTolerance" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfRiskTolerance_ai_rmf_risk_tolerance_influences_ai_rmf_risk_tolerance_influences" ON "AiRmfRiskTolerance_ai_rmf_risk_tolerance_influences" (ai_rmf_risk_tolerance_influences);
CREATE INDEX "ix_AiRmfRiskTolerance_ai_rmf_risk_tolerance_influences_AiRmfRiskTolerance_ai_rmf_id" ON "AiRmfRiskTolerance_ai_rmf_risk_tolerance_influences" ("AiRmfRiskTolerance_ai_rmf_id");

CREATE TABLE "AiRmfSubcategory" (
	id INTEGER NOT NULL,
	ai_rmf_subcategory_id TEXT NOT NULL,
	description TEXT NOT NULL,
	"AiRmfCategory_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfCategory_id") REFERENCES "AiRmfCategory" (id)
);
CREATE INDEX "ix_AiRmfSubcategory_id" ON "AiRmfSubcategory" (id);

CREATE TABLE "AiRmfImpact_ai_rmf_impact_affected_parties" (
	"AiRmfImpact_ai_rmf_id" TEXT,
	ai_rmf_impact_affected_parties VARCHAR(13),
	PRIMARY KEY ("AiRmfImpact_ai_rmf_id", ai_rmf_impact_affected_parties),
	FOREIGN KEY("AiRmfImpact_ai_rmf_id") REFERENCES "AiRmfImpact" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfImpact_ai_rmf_impact_affected_parties_AiRmfImpact_ai_rmf_id" ON "AiRmfImpact_ai_rmf_impact_affected_parties" ("AiRmfImpact_ai_rmf_id");
CREATE INDEX "ix_AiRmfImpact_ai_rmf_impact_affected_parties_ai_rmf_impact_affected_parties" ON "AiRmfImpact_ai_rmf_impact_affected_parties" (ai_rmf_impact_affected_parties);

CREATE TABLE "AiRmfSuggestedAction" (
	id INTEGER NOT NULL,
	ai_rmf_suggested_action_id TEXT NOT NULL,
	description TEXT NOT NULL,
	"AiRmfSubcategory_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfSubcategory_id") REFERENCES "AiRmfSubcategory" (id)
);
CREATE INDEX "ix_AiRmfSuggestedAction_id" ON "AiRmfSuggestedAction" (id);

CREATE TABLE "AiRmfDocumentationItem" (
	id INTEGER NOT NULL,
	ai_rmf_documentation_id TEXT NOT NULL,
	description TEXT NOT NULL,
	"AiRmfSubcategory_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfSubcategory_id") REFERENCES "AiRmfSubcategory" (id)
);
CREATE INDEX "ix_AiRmfDocumentationItem_id" ON "AiRmfDocumentationItem" (id);

CREATE TABLE "AiRmfResource" (
	id INTEGER NOT NULL,
	title TEXT NOT NULL,
	ai_rmf_resource_uuid TEXT NOT NULL,
	ai_rmf_resource_address TEXT,
	"AiRmfSubcategory_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfSubcategory_id") REFERENCES "AiRmfSubcategory" (id)
);
CREATE INDEX "ix_AiRmfResource_id" ON "AiRmfResource" (id);

CREATE TABLE "AiRmfSubcategory_ai_rmf_subcategory_about" (
	"AiRmfSubcategory_id" INTEGER,
	ai_rmf_subcategory_about TEXT,
	PRIMARY KEY ("AiRmfSubcategory_id", ai_rmf_subcategory_about),
	FOREIGN KEY("AiRmfSubcategory_id") REFERENCES "AiRmfSubcategory" (id)
);
CREATE INDEX "ix_AiRmfSubcategory_ai_rmf_subcategory_about_AiRmfSubcategory_id" ON "AiRmfSubcategory_ai_rmf_subcategory_about" ("AiRmfSubcategory_id");
CREATE INDEX "ix_AiRmfSubcategory_ai_rmf_subcategory_about_ai_rmf_subcategory_about" ON "AiRmfSubcategory_ai_rmf_subcategory_about" (ai_rmf_subcategory_about);

CREATE TABLE "AiRmfSubcategory_ai_rmf_subcategory_ai_actors" (
	"AiRmfSubcategory_id" INTEGER,
	ai_rmf_subcategory_ai_actors VARCHAR(36),
	PRIMARY KEY ("AiRmfSubcategory_id", ai_rmf_subcategory_ai_actors),
	FOREIGN KEY("AiRmfSubcategory_id") REFERENCES "AiRmfSubcategory" (id)
);
CREATE INDEX "ix_AiRmfSubcategory_ai_rmf_subcategory_ai_actors_AiRmfSubcategory_id" ON "AiRmfSubcategory_ai_rmf_subcategory_ai_actors" ("AiRmfSubcategory_id");
CREATE INDEX "ix_AiRmfSubcategory_ai_rmf_subcategory_ai_actors_ai_rmf_subcategory_ai_actors" ON "AiRmfSubcategory_ai_rmf_subcategory_ai_actors" (ai_rmf_subcategory_ai_actors);

CREATE TABLE "AiRmfSubcategory_ai_rmf_subcategory_topics" (
	"AiRmfSubcategory_id" INTEGER,
	ai_rmf_subcategory_topics TEXT,
	PRIMARY KEY ("AiRmfSubcategory_id", ai_rmf_subcategory_topics),
	FOREIGN KEY("AiRmfSubcategory_id") REFERENCES "AiRmfSubcategory" (id)
);
CREATE INDEX "ix_AiRmfSubcategory_ai_rmf_subcategory_topics_ai_rmf_subcategory_topics" ON "AiRmfSubcategory_ai_rmf_subcategory_topics" (ai_rmf_subcategory_topics);
CREATE INDEX "ix_AiRmfSubcategory_ai_rmf_subcategory_topics_AiRmfSubcategory_id" ON "AiRmfSubcategory_ai_rmf_subcategory_topics" ("AiRmfSubcategory_id");
