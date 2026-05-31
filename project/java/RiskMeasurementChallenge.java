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
  A challenge that complicates measurement of AI risks
(Part 1 §1.2.1).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RiskMeasurementChallenge extends NamedThing {

  private String challengeKind;


}