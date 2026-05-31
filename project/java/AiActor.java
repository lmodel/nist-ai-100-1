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
  An organization or individual that plays an active role in the AI
system lifecycle. AI actors include those who deploy or operate
AI as well as those who inform via formal or quasi-formal norms
and guidance (OECD 2019).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiActor extends NamedThingRMF {

  private List<String> actorTask;
  private List<String> lifecycleStage;
  private Boolean isTevv;
  private String audience;


}