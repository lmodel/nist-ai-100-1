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
  A stage of the AI lifecycle (Figure 2): Plan and Design,
Collect and Process Data, Build and Use Model, Verify and
Validate, Deploy and Use, or Operate and Monitor.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiLifecycleStage extends NamedThingRMF {

  private String stageKind;
  private Boolean includesTevv;


}