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
  A characteristic of a trustworthy AI system (Figure 4 / Part 1
§3). The seven characteristics are inter-related; addressing them
individually does not guarantee trustworthiness, and tradeoffs
are usually involved.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TrustworthinessCharacteristic extends NamedThingRMF {

  private String characteristicKind;
  private Boolean isBaseCondition;
  private Boolean isCrossCutting;


}