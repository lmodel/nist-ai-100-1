package None;

/* metamodel_version: 1.11.0 */
/* version: 1.0.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Root container that bundles the AI RMF Core (Functions) with
foundational concepts (trustworthiness characteristics,
lifecycle, actors, risks, harms), profiles, and Framework
attributes. Designed for serialising the Framework or a tailored
instance of it as a single JSON / YAML document.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiRmfFramework extends NamedThing {

  private AiRmfDocument document;
  private List<Function> functions;
  private List<TrustworthinessCharacteristic> trustworthinessCharacteristics;
  private List<AiLifecycleStage> lifecycleStages;
  private List<AiSystemDimension> dimensions;
  private List<AiActorTask> actorTasks;
  private List<AiRmfProfile> profiles;
  private List<RmfAttribute> attributes;
  private List<RiskMeasurementChallenge> riskMeasurementChallenges;
  private List<AiSpecificRisk> aiSpecificRisks;
  private List<HumanAiInteractionIssue> humanAiInteractionIssues;


}