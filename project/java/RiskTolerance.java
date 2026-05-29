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
  The organization's or AI actor's readiness to bear risk in order
to achieve its objectives (Adapted from ISO Guide 73). Risk
tolerance is highly contextual and application- and use-case
specific.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RiskTolerance extends NamedThing {

  private String toleranceStatement;
  private String legalBasis;


}