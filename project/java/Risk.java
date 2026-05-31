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
  The composite measure of an event's probability of occurring and
the magnitude or degree of the consequences of that event. When
considering negative impact, risk is a function of (1) the
negative impact or magnitude of harm and (2) the likelihood of
occurrence (Adapted from ISO 31000:2018; OMB Circular A-130:2016).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Risk extends NamedThing {

  private Float likelihood;
  private String magnitude;
  private String impactSign;
  private Boolean isResidual;
  private String riskResponse;
  private List<String> lifecycleStage;
  private List<String> trustworthinessCharacteristic;
  private List<Impact> relatedImpacts;
  private AiSystem affectsSystem;


}