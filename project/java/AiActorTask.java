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
  A category of task performed by AI actors (Appendix A). Each
task is associated with one or more lifecycle stages and a
typical set of actor roles.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiActorTask extends NamedThing {

  private String taskKind;
  private List<String> typicalActors;
  private List<String> lifecycleStage;
  private List<String> aiDimension;


}